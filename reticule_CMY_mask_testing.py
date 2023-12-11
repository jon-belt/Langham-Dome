from conversions import cmyConversion
import numpy as np
import cv2

i = 1
cyanL = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
magentaL = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
yellowL = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")

#this code runs through every possible value in the colour lists
### 1 ###
for cyan_value in cyanL:
    for magenta_value in magentaL:
        for yellow_value in yellowL:
            #counter so i know how close it is to being finished
            print(i)
            i=i+1
            img = cv2.imread(reticule_dot_path)
            if img is not None:
                conversion = cmyConversion(img)
                cmy_img = conversion[0]

                #create mask from the current parameters
                reticule_mask = (conversion[1] > cyan_value) & (conversion[2] < magenta_value) & (conversion[3] < yellow_value)     #1

                #create an output image
                result = np.zeros_like(cmy_img)
                result[reticule_mask] = cmy_img[reticule_mask]

                #saves image
                img_name = str("C"+str(cyan_value)+"_"+"M"+str(magenta_value)+"_"+"Y"+str(yellow_value)+".jpg")
                img_path = ("testing_images1/"+img_name)
                cv2.imwrite(img_path, result)
            else:
                print("Error: Unable to load the image.")

