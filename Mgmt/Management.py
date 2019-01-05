#(Traffic, Time, Road)

def UpdateTraffic(Inter):
	return Generate(Inter)


def Generate(x):							#Reset
	traff,time,j = x
	time = Time(traff)
	return (traff,time,j)

def Time(x):								#Update Time as Required
	traffic = x
	weight = 1.5

	if(x < 10):
		x = 10
	if(x > 60):
		weight = 1.2

	return traffic * weight


#def CheckLen(queue):						#Check if Queue is Empty
