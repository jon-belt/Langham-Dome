from locate_points import locateDot, locateReticule
import cv2
import numpy as np

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")

x = locateDot(three_dot_path)
y = locateReticule(three_dot_path)

print(x)
print(y)




