###  This code is now redundant as it was just used to find an general idea of the parameters.
###  It also used an now outdated and replaced version of 'locateDot' from 'yellowDot.py'
###  I am keeping this file here for now, so I have a documentation of my work, or if it is needed again in the future 

from conversions import cmyConversion
import numpy as np
import cv2
import time

i = 0
cyanL = [20]
magentaL = [90]
yellowL = [120]

reticuleDotPath = ("./imgs/reticuleAndDot.png")
dotPath = ("./imgs/dot.png")

#this code runs through every possible value in the colour lists
for cyan_value in cyanL:
    for magenta_value in magentaL:
        for yellow_value in yellowL:
            #counter so i know how close it is to being finished
            print(i)
            i=i+1
            img = cv2.imread(reticuleDotPath)
            if img is not None:
                conversion = cmyConversion(img)
                cmy_img = conversion[0]

                #create mask from the current parameters
                red_mask = (conversion[1] > cyan_value) & (conversion[2] < magenta_value) & (conversion[3] > yellow_value)

                #create an output image
                result = np.zeros_like(cmy_img)
                result[red_mask] = cmy_img[red_mask]

                #shows image
                cv2.imshow('Red Mask', result)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                #saves image
                img_name = str("C"+str(cyan_value)+"_"+"M"+str(magenta_value)+"_"+"Y"+str(yellow_value)+".jpg")
                img_path = ("testing_images/"+img_name)
                cv2.imwrite(img_path, result)
            else:
                print("Error: Unable to load the image.")



