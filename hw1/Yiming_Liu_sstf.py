#Shortest Seek Time First
#@author:YimingLiu
import sys

def SSTF():
	data = open(sys.argv[1],"r")

	line1 = data.readline()
	position = int(line1)

	line  = data.readline()
	queue = line.split()  #split every string and save
	request_queue = map(int,queue) #str to int

	seek_time = 0
	
	max_dis = max(request_queue)
	min_seek_time = abs(position - max_dis)
	request_queue.sort() #sort the queue from small to big

	while len(request_queue) > 0:

		for request in request_queue:   #find the current shortest distance from position
			seek_t = abs(position - request)
			if seek_t < min_seek_time:
				min_seek_time = seek_t
				buf = request

		seek_time += abs(position - buf)  
		position = buf
		request_queue.remove(buf)  #delete the nearest request from request_queue 
		min_seek_time = abs(position - max_dis)
		buf = max_dis
		

	print seek_time


if __name__ == '__main__':
	SSTF()