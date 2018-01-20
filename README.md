# pdf-to-images
These scripts are for use in image based pdf text extraction. The intent is to take a .pdf, convert it to image/images based on the page count. Take each image and clean it up a little then extract the text outputting it to a text file.
Libraries used:
pytesseract
OpenCV
wand
pillow

On Ubuntu: Python 3.5.4 :: Anaconda custom (64-bit)

1) Go through the installs.txt:
   Everyone is set up on different operating systems and python enviorments.
   You potentially need/do not need some of these libraries.
2) cmdline_convert.py:
   This basically runs the "CONVERT" from the command line and passes in the required .pdf and output file.
3) image_cleanup.py:
   This uses openCV to try and clean up the image to make the text more prevalent.
3) text_from_image.py:
   This is where the image is analyzed and the text is pulled for output to a .txt file.
