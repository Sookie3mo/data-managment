#First Come First Seek
#@author:YimingLiu
import sys


def FCFS():
	data = open(sys.argv[1],"r")

	line1 = data.readline()
	position = int(line1)

	line  = data.readline()
	queue = line.split() #split every string and save
	request_queue = map(int,queue) #str to int

	seek_time = 0
	
	for request in request_queue:
		seek_time += abs(request-position)
		position = request
	print(seek_time)



if __name__ == '__main__':
	FCFS() 