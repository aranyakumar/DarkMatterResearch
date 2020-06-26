"""
   This class creates false ellipses
    in granite images to test the users'
    ability to detect ellipses 
"""
        
#importing OpenCV
import cv2
import numpy as np

image = cv2.imread('granite.jpg', cv2.IMREAD_COLOR) #read the RGB image
class EllipseOverlay:
     
    def drawEllipse():
        ellipse = cv2.ellipse(image,(256,256),(100,50),0,0,180,255,-1)
        cv2.imshow('image', image) #show the image
        cv2.waitkey(0) #waits for the key press

    def main():
        drawEllipse()

