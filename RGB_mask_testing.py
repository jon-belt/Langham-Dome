from conversions import cmyConversion
import numpy as np
import cv2
import time

i = 0
#values before being swapped
# redL = [120]     
# greenL = [210]
# blueL = [125]

redL = [125]
greenL = [210]
blueL = [125]

reticuleDotPath = ("./imgs/reticuleAndDot.png")
dotPath = ("./imgs/dot.png")

#this code runs through every possible value in the colour lists
for red_value in redL:
    for green_value in greenL:
        for blue_value in blueL:
            #counter so i know how close it is to being finished
            print(i)
            i=i+1
            img = cv2.imread(reticuleDotPath)
            if img is not None:
                #split channels for CMY conversion
                blue_channel, green_channel, red_channel = cv2.split(img)

                # create a red colour mask, capturing a range of red shades
                red_mask = (red_channel > red_value) & (green_channel < green_value) & (blue_channel < blue_value)

                # create an output image with only the red regions
                result = np.zeros_like(img)
                result[red_mask] = img[red_mask]

                cv2.imshow('Red Mask', result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                img_name = str("R"+str(red_value)+"_"+"G"+str(green_value)+"_"+"B"+str(blue_value)+".jpg")
                img_path = ("testing_images/"+img_name)
                cv2.imwrite(img_path, result)
            else:
                print("Error: Unable to load the image.")

