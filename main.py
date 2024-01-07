from locate_points import locateDot, getReticule
import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, crop

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")

locateDot(reticule_dot_path)
getReticule(reticule_dot_path)




