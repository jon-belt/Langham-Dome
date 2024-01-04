import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask, getDotContours, getReticuleContours


def reticuleTemplate(imagePath):
    #load in current frame & make copy
    img = cv2.imread(imagePath, 0)

    #load in template, convert to cmy, then convert to greyscale
    ret = cv2.imread("./templates/ret2.png")
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

        bottom_right = (location[0] + w, location[1] + h)
        cv2.rectangle(img2, location, bottom_right, 255, 5)

        cv2.imshow("Match", img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows