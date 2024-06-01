import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask, getDotContours, getReticuleContours, crop

# Load the image
reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
#dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")
three_dot_path2 = ("./imgs/3dots2.png")
good_score = ("./imgs/good_score.png")
bad_score = ("./imgs/bad_score.png")

templatePath = ("./templates/ret1.png")
template = cv2.imread(templatePath)
cmy_template = cmyConversion(template)

testingImages = [reticule_path, reticule_dot_path, three_dot_path, three_dot_path2, good_score, bad_score]

dp = 1
minDist = 440
param1 = 10
param2 = 5
minRadius = int(410/2)
maxRadius = int(440/2)

for path in testingImages:
    img2 = cv2.imread(path)
    img2 = crop(img2)

    #convert to grayscale
    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    #apply Gaussian blur
    gray_blurred = cv2.GaussianBlur(gray, (1, 1), 0)

    #apply hough circle transform
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp, minDist, param1=param1, param2=param2, minRadius=minRadius, maxRadius=maxRadius)

    #draw circles that are detected
    if circles is not None:
        circles = np.uint16(np.around(circles))
        # Access the first circle in the list of circles
        first_circle = circles[0, 0]
        center = (first_circle[0], first_circle[1])
        print(first_circle[0], first_circle[1])