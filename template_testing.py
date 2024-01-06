import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask, getDotContours, getReticuleContours

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")
three_dot_path2 = ("./imgs/3dots2.png")
test_path = ("./testing_images1/three_dot_path2.png")

#load in current frame & make copy
img = cv2.imread(reticule_path)
img = cv2.imread(reticule_dot_path)
img = cv2.imread(three_dot_path)
#img = cv2.imread(test_path)
img = cmyConversion(img)
img = reticuleMask(img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#load in template, convert to cmy, then convert to greyscale
ret = cv2.imread("./templates/ret1.png")
#ret_cmy = cmyConversion(ret)
template = cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY)

#find height and width for template
h, w = template.shape

#find best method
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, cv2.TM_CCORR)

    #sets min and max location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #if method is either variation of SQDIFF, use the min loc, if not use the max loc
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
        #location = max_loc
    else:
        location = max_loc
        #location = min_loc

    #finds the boundaries of the rectangle, and places it on our greyscaled image
    bottom_right = (location[0] + w, location[1] + h)
    print(bottom_right)
    print(max_val)
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    cv2.imshow("Match", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows