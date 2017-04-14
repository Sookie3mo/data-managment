#C-Look  Assuming we look from outer to inner(199 -> 0) and ignore the jumping time
#@author:YimingLiu
import sys

def CLOOK():
	data = open(sys.argv[1],"r")

	line1 = data.readline()
	position = int(line1)

	line  = data.readline()
	queue = line.split()  #split every string and save
	request_queue = map(int,queue) #str to int

	seek_time = 0

	request_queue.sort() #sort the queue from min to max
	head = min(request_queue)
	tail = max(request_queue)
	queue1 = []
	queue2 = []

	if position < head:
		seek_time = tail - head

	elif position > tail:
		seek_time = position - head
	
	else: #if position is in the middle, it splits the queue into two parts
		for i in range(0,len(request_queue)):
			if position > request_queue[i]:
				queue1.append(request_queue[i])
			else:
				queue2.append(request_queue[i])
		
		head2 = min(queue2)
		if len(queue2)>1: #the case if 2+ requests outter than position
			seek_time = position - head + tail - head2
		else:
			seek_time = position -head  #the case if only 1 request outter than position

	print seek_time


if __name__ == '__main__':
	CLOOK()  
	