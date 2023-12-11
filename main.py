from locate_points import locateDot
import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")

locateDot(three_dot_path)
locateDot(dot_path)
locateDot(reticule_path)


