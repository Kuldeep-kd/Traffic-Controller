import cv2
from Hack import Capture

for x in range(4):
    for y in range(4):
        strg = "Media/"+ str(x+1) +"/"+str(y+1)+".jpg"

        print(Capture( (strg,y) ))