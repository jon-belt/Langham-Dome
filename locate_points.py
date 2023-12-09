import cv2
import numpy as np
from conversions import cmyConversion

def locateDot(imagePath, cyan, magenta, yellow):
    img = cv2.imread(imagePath)
    if img is not None:
        conversion = cmyConversion(img)
        cmy_img = conversion[0]

        # create a red colour mask, capturing a range of red shades
        red_mask = (conversion[1] > cyan) & (conversion[2] < magenta) & (conversion[3] < yellow)

        # create an output image with only the red regions
        result = np.zeros_like(cmy_img)
        result[red_mask] = cmy_img[red_mask]

        cv2.imshow('Red Mask', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Error: Unable to load the image.")

