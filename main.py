#from locate_points import locateDot, locateReticule, reticuleTemplate
from template_testing import reticuleTemplate
import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")

reticuleTemplate(reticule_path)

#template matching methods:
#methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]




