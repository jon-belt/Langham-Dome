import cv2
import numpy as np

def locateDot(imagePath, red_nums, green_nums, blue_nums):
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
        red_mask = (red_channel > red_nums) & (green_channel < green_nums) & (blue_channel < blue_nums)

        # create an output image with only the red regions
        result = np.zeros_like(img)
        result[red_mask] = img[red_mask]

        # cv2.imshow('Red Mask', result)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        print("Error: Unable to load the image.")

