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
    #load in current frame & make copy
    img = cv2.imread(imagePath, 0)

    #load in template, convert to cmy, then convert to greyscale
    ret = cv2.imread("./templates/ret3.png")
    ret_cmy = cmyConversion(ret)
    template = cv2.cvtColor(ret_cmy, cv2.COLOR_BGR2GRAY)

    #find height and width for template
    h, w = template.shape

    #find best method
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    for method in methods:
        img2 = img.copy()

        result = cv2.matchTemplate(img2, template, method)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(min_loc, max_loc)
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
        else:
            location = max_loc





    




    # cv2.imshow("", template)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    print("")