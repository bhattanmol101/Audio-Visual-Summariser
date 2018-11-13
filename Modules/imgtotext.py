from picamera import PiCamera 
from time import sleep 
import pytesseract 
from PIL import Image


camera = PiCamera(resolution=(2580, 1920))
camera.capture('../Desktop/image.jpg')

img = Image.open('../Desktop/image.jpg')

txt = pytesseract.image_to_string(img)

print(txt)
