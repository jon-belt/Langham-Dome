from yellowDot import locateDot
import cv2
import time

red = 255
green = 255
blue = 255
i = 0

redL = [125]
greenL = [210]
blueL = [119]
#it takes 71 seconds to compile all images

reticuleDotPath = ("img/reticuleAndDot.png")

# start_time = time.time()
# locateDot(reticuleDotPath, red, green, blue)
# end_time = time.time()

# elapsed_time = end_time - start_time
# print(elapsed_time)

for red_value in redL:
    for green_value in greenL:
        for blue_value in blueL:
            #counter so i know how close it is to being finished, i = 2743
            print(i)
            i=i+1
            locateDot(reticuleDotPath, red_value, green_value, blue_value)

