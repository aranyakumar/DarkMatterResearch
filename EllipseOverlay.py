# importing cv2 
import cv2 
import argparse
import random
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2lab, deltaE_cie76
from image_slicer import slice

# Cut image into 4 subsections
#im = cv2.imread('graniteSlab.jpeg')
tiles = slice('D:\Dark Matter Research 2020\DarkMatterResearch\agranite.jpg', 4)

# Path
im = cv2.imread("granite_02_02.png")
im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)

# Construct arg parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())
    
# Reading an image in default mode getting width and height
image = im
(width, height, channel) = image.shape  

### Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)               #convert to gray
### Apply a Gaussian blur to the image
gray = cv2.blur(gray, (10, 10))
### Find the darkest and brightest region
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    
# Window name in which image is displayed 
window_name = 'Image'
   
center_coordinates = (random.randint(10, width), random.randint(10, height)) 
  
axesLength = (25, 40) 
  
angle = random.randint(0,360)
  
startAngle = 0
  
endAngle = 360

refPt = []
cropping = False

def click_and_crop(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x,y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x,y))
        cropping = False

        cv2.rectangle(image, refPt[0], refPt[1], (0,255,0), 2)
   
# Gets darkest color in the image 
#color = (minVal, minVal, minVal) 
color = np.random.normal(center_coordinates[0],minVal,(10,10))
   
# Line thickness of -1 px 
thickness = -1
   
# Using cv2.ellipse() method 
# Draw a ellipse with blue line borders of thickness of -1 px 
ellipse = cv2.ellipse(image, center_coordinates, axesLength, 0, 
                          0, 180, (255,255,255), -1) 
ellipseImage = cv2.minAreaRect(ellipse)

# Creating noise
noise = np.random.normal(1000., 1000., (1000, 1000, 3))
granite = cv2.imwrite("ellipseImage", noise)

def overlay(img, img_overlay, alpha_mask):
	y1, y2 = max(0, center_coordinates[1]), min(img.shape[0], center_coordinates[1] + img_overlay.shape[0])
	x1, x2 = max(0, center_coordinates[0]), min(img.shape[1], center_coordinates[0] + img_overlay.shape[1])

    # Overlay ranges
	y1o, y2o = max(0, -center_coordinates[1]), min(img_overlay.shape[0], img.shape[0] - center_coordinates[1])
	x1o, x2o = max(0, - center_coordinates[0]), min(img_overlay.shape[1], img.shape[1] - center_coordinates[0])

    # Exit if nothing to do
	if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
		return

	channels = img.shape[2]

	alpha = alpha_mask[y1o:y2o, x1o:x2o]
	alpha_inv = 1.0 - alpha

	for c in range(channels):
		img[y1:y2, x1:x2, c] = (alpha * img_overlay[y1o:y2o, x1o:x2o, c] +
								alpha_inv * img[y1:y2, x1:x2, c])

# Displaying the image 
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	cv2.setMouseCallback("image", click_and_crop)
	key = cv2.waitKey(1) & 0xFF
	# if the 'r' key is pressed, reset the cropping region
	if key == ord("r"):
		image2 = image.copy()
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break
if len(refPt) == 2:
	roi = image[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)
	print(minVal)
	print(maxVal)
	cv2.imshow("Blur", gray)
	cv2.imshow('False Ellipse', image)
	cv2.imwrite("granite_04_fake.png", image)
	cv2.waitKey(0)
	cv2.imshow("image", image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
