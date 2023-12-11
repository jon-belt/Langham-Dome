from conversions import cmyConversion
import numpy as np
import cv2


i = 0
cyanL = [20]
magentaL = [90]
yellowL = [120]

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")

#this code runs through every possible value in the colour lists
for cyan_value in cyanL:
    for magenta_value in magentaL:
        for yellow_value in yellowL:
            #counter so i know how close it is to being finished
            print(i)
            i=i+1
            img = cv2.imread(dot_path)
            if img is not None:
                conversion = cmyConversion(img)
                cmy_img = conversion[0]

                #create mask from the current parameters
                dot_mask = (conversion[1] > cyan_value) & (conversion[2] < magenta_value) & (conversion[3] > yellow_value)

                #create an output image
                result = np.zeros_like(cmy_img)
                result[dot_mask] = cmy_img[dot_mask]

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



