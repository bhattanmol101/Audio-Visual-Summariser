import speech_recognition as sr
import time
import sys

def recog(lon):
	f = open("speechnotes.txt","w+")
	f.close()
	r = sr.Recognizer()
	t = time.time()
	while 1:
		with sr.Microphone() as source:
			print("saysomething")
			audio = r.listen(source)
			#if((time.time()-t)<int(lon)):
			#	print(time.time()-t)
			#else:
			#	print("exiting")
			#	sys.exit(0)
		try:
			s = r.recognize_google(audio)
			print(s)
			f = open("speechnotes.txt","a")
			f.write(s +".")
			f.close()
		except sr.UnknownValueError:
			continue
		except sr.RequestError as e:
			continue
recog(100)
