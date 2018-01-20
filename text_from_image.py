import os
from pytesseract import image_to_string
from PIL import Image

txtstring = image_to_string(Image.open('images/s-0.png'), lang='eng')
with open ("Output.txt","w")as fp1:
	fp1.write(txtstring)
fp1.close()