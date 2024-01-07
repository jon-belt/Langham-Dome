import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask, getDotContours, getReticuleContours

# Load the image
reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")
three_dot_path2 = ("./imgs/3dots2.png")
good_score = ("./imgs/bad_score.png")
bad_score = ("./imgs/good_score.png")

cs1 = [cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV, cv2.COLOR_BGR2LAB, cv2.COLOR_BGR2HLS, cv2.COLOR_BGR2LAB, cv2.COLOR_BGR2LUV,
       cv2.COLOR_BGR2XYZ, cv2.COLOR_BGR2YCrCb]
cs2 = [cv2.COLOR_BGR2BGRA]
count = 1

for c1 in cs1:
    for c2 in cs2:
        img = cv2.imread(reticule_path)
        print(str(count) + "   "+(str(c1) +" "+ str(c2)))
        count = count+1
        #img = cmyConversion(img)

        img2 = cv2.cvtColor(img, c1)
        result = cv2.cvtColor(img2, c2)


        # Show the result
        cv2.imshow('result', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()