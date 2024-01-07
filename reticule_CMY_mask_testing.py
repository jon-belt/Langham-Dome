from conversions import cmyConversion
import numpy as np
import cv2

i = 1
blueH = [88]
greenH = [72]
redH = [80]

blueL = [42]
greenL = [10]
redL = [36]

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
three_dot_path = ("./imgs/3dots.png")
three_dot_path2 = ("./imgs/3dots2.png")

#this code runs through every possible value in the colour lists
img = cv2.imread(three_dot_path2)
cmy_img = cmyConversion(img)
for blue_lower in blueL:
    for green_lower in greenL:
        for red_lower in redL:
            for blue_higher in blueH:
                for green_higher in greenH:
                    for red_higher in redH:
                        #counter so i know how close it is to being finished
                        print(i)
                        i=i+1
                        # img = cv2.imread(reticule_dot_path)
                        # cmy_img = cmyConversion(img)

                        #applies mask
                        lower_mask = np.array([blue_lower, green_lower, red_lower], dtype = "uint8")
                        upper_mask= np.array([blue_higher, green_higher, red_higher], dtype = "uint8")

                        mask = cv2.inRange(cmy_img, lower_mask, upper_mask)

                        result = cv2.bitwise_and(cmy_img, cmy_img, mask = mask)

                        #shows image
                        cv2.imshow('Masked Image', result)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()

                        # #saves image
                        # img_name = str("LB"+str(blue_lower)+"_"+"G"+str(green_lower)+"_"+"R"+str(red_lower)+"_HB"+str(blue_higher)+"_"+"G"+str(green_higher)+"_"+"R"+str(red_higher)+".jpg")
                        # img_path = ("testing_images1/"+img_name)
                        # cv2.imwrite(img_path, result)


