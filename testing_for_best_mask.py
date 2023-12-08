from yellowDot import locateDot
import cv2
import time

red = 255
green = 255
blue = 255
i = 0

redL = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 255]
greenL = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 255]
blueL = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 255]
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
            #print(i*elapsed_time)
            i=i+1