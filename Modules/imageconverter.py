import pytesseract 
from PIL import Image 
import time

f = open("imagenotes.txt","w+")
f.close()

def convert():
	f = open("imagenotes.txt","a")
	img = Image.open('img.png')
	txt = pytesseract.image_to_string(img)
	print(txt)
	f.write(txt)
	f.close()
	time.sleep(10)
