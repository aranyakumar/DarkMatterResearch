# importing cv2 
import cv2 
import argparse
import random
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2lab, deltaE_cie76
import image_slicer

# Cut image into 4 subsections
#im = cv2.imread('graniteSlab.jpeg')
tiles = image_slicer.slice('graniteSlab.jpeg', 4)

# Path
im = cv2.imread("graniteSlab_02_02.png")

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
  
axesLength = (15, 10) 
  
angle = random.randint(0,360)
  
startAngle = 0
  
endAngle = 360
   
# Gets darkest color in the image 
color = (minVal, minVal, minVal) 
   
# Line thickness of -1 px 
thickness = -1
   
# Using cv2.ellipse() method 
# Draw a ellipse with blue line borders of thickness of -1 px 
image = cv2.ellipse(image, center_coordinates, axesLength, angle, 
                          startAngle, endAngle, color, -1) 

# Creating noise
noise = np.random.normal(1000., 1000., (1000, 1000, 3))
granite = cv2.imwrite("gaussian_noise.png", noise)
   
# Displaying the image 
print(minVal)
print(maxVal)
cv2.waitKey(0)
cv2.imshow("Blur", gray)
cv2.imshow('False Ellipse', image)
cv2.waitKey(0)
cv2.imwrite("granite_04_fake.png", image)
cv2.destroyAllWindows()
