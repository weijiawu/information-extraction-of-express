# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
import numpy as np

# construct the argument parse and parse the arguments


# load the example image and convert it to grayscale
image = cv2.imread(r'C:\Users\admin\Desktop\git\test\project\picture1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# if len(image.shape) == 3 or len(image.shape) == 4:
#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# else:
#     gray = image

# check to see if we should apply thresholding to preprocess the
# image
gray = cv2.threshold(gray, 0,255 ,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
kernel = np.ones((5, 5), np.uint8)
gray = cv2.dilate(gray, kernel, iterations=1)
gray1 = gray 
# gray = cv2.dilate(gray, kernel, iterations=1)
# gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
# gray = cv2.Canny(gray,350,500)
gray1 = gray

height,width = gray.shape

##反色
for i in range(height):
     for j in range(width):
        gray[i,j] = (255-gray[i,j]) 

cv2.imshow("Image1", gray)

gray = cv2.GaussianBlur(gray, (9, 9),0)
(_, gray) = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25))
gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

gray = cv2.erode(gray, None, iterations=3)
gray = cv2.dilate(gray, None, iterations=20)
 
cv2.imshow("Image2", gray)

##画框
cnts,contours,hierarchy= cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
c = sorted(contours, key = cv2.contourArea, reverse = True)[0]

# compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = np.int0(cv2.boxPoints(rect))

# draw a bounding box arounded the detected barcode and display the image


gray = cv2.drawContours(image.copy(),[box],-1, (0, 255, 0), 3)
cv2.imshow("Image3", gray)
#  抠图
Xs = [i[0] for i in box]
Ys = [i[1] for i in box]
x1 = min(Xs)
x2 = max(Xs)
y1 = min(Ys)
y2 = max(Ys)
hight = y2 - y1
width = x2 - x1
gray= gray[y1:y1+hight, x1:x1+width]

cv2.imshow("Image4", gray)
           
 ##提取字母数字          
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0,255 ,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
gray = cv2.medianBlur(gray, 3)

kernel = np.ones((5, 5), np.uint8)
gray = cv2.dilate(gray, kernel, iterations=1)

gray = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

gray = cv2.dilate(gray, None, iterations=1)

cv2.imshow("Image5", gray)

##反色
height,width = gray.shape
for i in range(height):
     for j in range(width):
        gray[i,j] = (255-gray[i,j]) 
cv2.imshow("Image6", gray)
           
##识别
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

# show the output images
# cv2.imshow("Output1", gray1)
cv2.waitKey(0)
cv2.destroyAllWindows()