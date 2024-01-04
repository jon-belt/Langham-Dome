import sys
from locate_points import locateDot
import cv2
import time

i = 0
redL = [120]
greenL = [210]
blueL = [125]
dot_amount = 0

reticuleDotPath = ("./img/reticuleAndDot.png")
DotPath = ("./img/dot.png")

for red_value in redL:
    for green_value in greenL:
        for blue_value in blueL:
            #counter so i know how close it is to being finished
            print(i)
            i=i+1

            



