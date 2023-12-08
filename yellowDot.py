import cv2
import numpy as np

def locateDot(imagePath, red, green, blue):
    img = cv2.imread(imagePath)
    if img is not None:
        #split channels for CMY conversion
        blue_channel, green_channel, red_channel = cv2.split(img)

        #calculate the CMY channels
        cyan_channel = 1 - red_channel
        magenta_channel = 1 - green_channel
        yellow_channel = 1 - blue_channel

        #merge the CMY channels into a single image
        cmy_img = cv2.merge((cyan_channel, magenta_channel, yellow_channel))

        #display CMY image
        # cv2.imshow('CMY Image', cmy_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # create a red colour mask, capturing a range of red shades
        red_mask = (red_channel > red) & (green_channel < green) & (blue_channel < blue)

        # create an output image with only the red regions
        result = np.zeros_like(img)
        result[red_mask] = img[red_mask]

        # cv2.imshow('Red Mask', result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        img_name = str("R"+str(red)+"_"+"G"+str(green)+"_"+"B"+str(blue)+".jpg")
        img_path = ("testing images/"+img_name)
        cv2.imwrite(img_path, result)
    else:
        print("Error: Unable to load the image.")

