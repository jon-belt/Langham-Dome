import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask, getDotContours, getReticuleContours

def locateDot(imagePath):
    img = cv2.imread(imagePath)
    if img is not None:
        img = cv2.imread(imagePath)
        img_contour = img.copy()

        #reads in img, and performs transformations
        img_cmy = cmyConversion(img)
        img_dots = dotMask(img_cmy)
        img_dots_blur = cv2.GaussianBlur(img_dots, (7, 7), 1)
        img_dots_grey = cv2.cvtColor(img_dots_blur, cv2.COLOR_BGR2GRAY)

        img_canny = cv2.Canny(img_dots_grey, 150, 225)

        #help reduce noise
        kernel = np.ones((5,5))
        img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

        #runs get contours function and populates 'img_contour'
        getDotContours(img_dilate, img_contour)
    else:
        print("Error: Unable to load the image.")

def locateReticule(imagePath):
    img = cv2.imread(imagePath)
    if img is not None:

        #reads every frame in, performs CMY conversion and applies the mask for the dots
        img_cmy = cmyConversion(img)
        img_reticule = reticuleMask(img_cmy)
        img_reticule_blur = cv2.GaussianBlur(img_reticule, (9, 9), 1)

        img_canny = cv2.Canny(img_reticule_blur, 225, 145)

        #help reduce noise
        kernel = np.ones((5,5))
        img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

        #runs get contours function and populates 'img_contour'
        getReticuleContours(img_dilate)
    else:
        print("Error: Unable to load the image.")