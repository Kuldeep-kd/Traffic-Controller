import cv2
import matplotlib.pyplot as plt
from Mgmt.Management import UpdateTraffic

traffic = [-1,-1,-1,-1]
vehicle_cascade = cv2.CascadeClassifier("Cascade.xml")
plt.suptitle("Traffic Coordinator")

def Capture(data):
	footage,index = data

	image = cv2.imread(footage)

	RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	Gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blur = cv2.GaussianBlur(Gray,(5,5),0)
	vehicle = vehicle_cascade.detectMultiScale(blur,1.01,3)

	traffic[index] = len(vehicle)

	Inter = (traffic[index],0,index)
	
	update = UpdateTraffic(Inter)
	
	plot = plt.subplot(2,2,index+1)
	plot.set_title(f"Traffic : {update[0]} | Time : {update[1]} | Road : {update[2]+1}")
	plt.imshow(RGB)

	if(index == 3 and not -1 in traffic):
		plt.show()

	return update



