import pymongo
import time
import datetime

def senddni(topic, name, fname):
	ts = time.time()+19800
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	client = pymongo.MongoClient("mongodb+srv://anmolbhat:Eminem1710@cluster0-wiztd.gcp.mongodb.net/test?retryWrites=true")
	db = client.self_study
	collection = db.detailed_notes_images

	f = open(str(fname)+".txt","r")
	s = f.read()
	#print(s)

	data = {
		"Lecture Topic":str(topic),
		"Lecturer's Name":str(name),
		"Timestamp":str(st),
		"Notes":str(s)
		}

	collection.insert_one(data)
	#print("data inserted")

def senddns(topic, name, fname):
	ts = time.time()+19800
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	client = pymongo.MongoClient("mongodb+srv://anmolbhat:Eminem1710@cluster0-wiztd.gcp.mongodb.net/test?retryWrites=true")
	db = client.self_study
	collection = db.detailed_notes_speech

	f = open(str(fname)+".txt","r")
	s = f.read()
        #print(s)

	data = {
		"Lecture Topic":str(topic),
		"Lecturer's Name":str(name),
		"Timestamp":str(st),
		"Notes":str(s)
		}
	collection.insert_one(data)
	#print("Data inserted")

def sendsni(topic, name, fname):
	ts = time.time()+19800
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	client = pymongo.MongoClient("mongodb+srv://anmolbhat:Eminem1710@cluster0-wiztd.gcp.mongodb.net/test?retryWrites=true")
	db = client.self_study
	collection = db.summarized_notes_images

	f = open(str(fname)+".txt","r")
	s = f.read()
#        print(s)
	data = {
		"Lecture Topic":str(topic),
		"Lecturer's Name":str(name),
		"Timestamp":str(st),
		"Notes":str(s)
		}

	collection.insert_one(data)
	#print("Data Send")

def sendsns(topic, name, fname):
	ts = time.time()+19800
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

	client = pymongo.MongoClient("mongodb+srv://anmolbhat:Eminem1710@cluster0-wiztd.gcp.mongodb.net/test?retryWrites=true")
	db = client.self_study
	collection = db.summarized_notes_speech

	f = open(str(fname)+".txt","r")
	s = f.read()
	#print(s)

	data = {
		"Lecture Topic":str(topic),
		"Lecturer's Name":str(name),
		"Timestamp":str(st),
		"Notes":str(s)
		}

	collection.insert_one(data)
	#print("Data DOne")

