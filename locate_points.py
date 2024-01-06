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
        #reads a frame in, performs CMY conversion and applies the mask for the dots
        img_cmy = cmyConversion(img)
        img_reticule = reticuleMask(img_cmy)
        img_reticule_blur = cv2.GaussianBlur(img_reticule, (9, 9), 1)
        img_dots_grey = cv2.cvtColor(img_reticule_blur, cv2.COLOR_BGR2GRAY)

        img_canny = cv2.Canny(img_reticule, 225, 145)

        #help reduce noise
        kernel = np.ones((5,5))
        img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

        #runs get contours function and populates 'img_contour'
        getReticuleContours(img_dilate)
    else:
        print("Error: Unable to load the image.")

def reticuleTemplate(imagePath):
    #loads in and converts img to cmy, then greyscale
    img = cv2.imread(imagePath)
    img = cmyConversion(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #loads in and converts template to cmy, then greyscale
    ret = cv2.imread("./templates/ret1.png")
    ret_cmy = cmyConversion(ret)
    template = cv2.cvtColor(ret_cmy, cv2.COLOR_BGR2GRAY)

    #find height and width for template, this allows us to find the centre of the template later on
    h, w = template.shape

    result = cv2.matchTemplate(img, template, cv2.TM_CCORR)

    #sets min and max location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #finds bottom right corner of template, then finds centre point of template through a basic transformation
    bottomRight = (min_loc[0] + w, min_loc[1] + h)

    #finds x center and adjusts appropriately as the template match is off
    centreX = np.round(bottomRight[0]-(w/2))
    centreX = centreX+5

    #finds y center and adjusts appropriately as the template match is off
    centreY = np.round(bottomRight[1]-(h/2))

    #x works well, but the y is sometimes off.  This means i will need to find a way to edit the y's offset apprioriately

    yOffset = 80

    centreY = centreY+yOffset
    print(centreX, centreY)