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

    def detect():
        params = cv2.SimpleBlobDetector_Params()

        params.filterByArea = True
        params.minArea = 10

        params.filterByCircularity = True 
        params.minCircularity = 0.7

        params.filterByConvexity = True
        params.minConvexity = 0.5

        params.filterByInertia = True
        params.minInertiaRatio = 0.01

        detector = cv2.SimpleBlobDetector_create(params)

        keypoints = detector.detect(image)

        blank = np.zeros((1, 1))  
        blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), 
                          cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS) 

        number_of_blobs = len(keypoints) 
        text = "Number of Circular Blobs: " + str(len(keypoints)) 
        cv2.putText(blobs, text, (20, 550), 
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2) 

        cv2.imshow("Filtering Circular Blobs Only", blobs) 
        cv2.waitKey(0) 
        cv2.destroyAllWindows() 
     
    def drawEllipse():
        ellipse = cv2.ellipse(image,(256,256),(100,50),0,0,180,255,-1)
        cv2.imshow('image', image) #show the image
        cv2.waitkey(0) #waits for the key press

    def main():
        detect()
        drawEllipse()

    if __name__ == '__main__':
        detect()
        drawEllipse()

