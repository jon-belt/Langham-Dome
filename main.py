from locate_points import locateDot
import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")

locateDot(reticule_dot_path)

img = cv2.imread(reticule_dot_path)
img2 = cv2.imread(reticule_dot_path)

cmy_img = cmyConversion(img)
cmy_img2= cmyConversion(img2)





