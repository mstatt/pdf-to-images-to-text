#This cleans up the image for text extraction
import os
import cv2


filename = "PATH/NAME.png"
newfile = "PATH/clean_"+ os.path.basename(filename)
img = cv2.imread(filename, 0)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
cv2.imwrite(newfile, thresh)