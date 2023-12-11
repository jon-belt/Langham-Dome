from locate_points import locateDot
import cv2
import numpy as np
from conversions import cmyConversion
from stack_images import stackImages
from masks import dotMask

#values for these variables were derived from trial and error through the 'testing_for_best_mask.py' script i wrote
#values are solely based on the phone video

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")

img = cv2.imread(three_dot_path)
cmy_img = cmyConversion(img)
masked_img = dotMask(cmy_img)

cv2.imshow('Masked Image', masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


