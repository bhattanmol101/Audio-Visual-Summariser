import MongoDBcon
import summarize
import time
import sys

def start_back(s):
	data = s.split(",")
	print("Going to Sleep")
	time.sleep(int(int(data[2])*110))
	print("Waking")
	summarize.summ()
	print("Notes Summarized")
	MongoDBcon.senddni(str(data[0]),"Prof. "+str(data[1]),"imagenotes")
	print("Data 1 Sent")
	MongoDBcon.senddns(str(data[0]),"Prof. "+str(data[1]),"imgnotessumm")
	print("Data 2 Sent")
	MongoDBcon.sendsni(str(data[0]),"Prof. "+str(data[1]),"speechnotes")
	print("Data 3 Sent")
	MongoDBcon.sendsns(str(data[0]),"Prof. "+str(data[1]),"speechnotessumm")
	print("Data 4 Sent")
	sys.exit()
