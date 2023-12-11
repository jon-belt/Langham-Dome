import cv2
import numpy as np

def dotMask(img):
    #create a red colour mask, capturing a range of red shades
    #BGR
    lower_mask = np.array([40, 50, 100], dtype = "uint8")
    upper_mask= np.array([65, 70, 250], dtype = "uint8")

    mask = cv2.inRange(img, lower_mask, upper_mask)

    masked_img = cv2.bitwise_and(img, img, mask = mask)

    return masked_img