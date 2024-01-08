 #this script holds all image transformation functions
import cv2
import numpy as np
from conversions import cmyConversion

#a function that crops the frame so that only the projection is visible
def crop(img):
    cmy_img = cmyConversion(img)    #cmy conversion

    #colour mask to separate projection from wall
    lower_mask = np.array([30, 10, 40], dtype = "uint8")
    upper_mask= np.array([105, 100, 100], dtype = "uint8")
    mask = cv2.inRange(cmy_img, lower_mask, upper_mask)

    #find contours of the masked image
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        #uses largest contour
        contour = max(contours, key=cv2.contourArea)
        cv2.drawContours(img, [contour], -1, (0, 255, 0), 2)

        #approximate the contour
        epsilon = 0.05 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        #find the coords
        top_left, bot_left, top_right, bot_right = approx.reshape(4, 2)

        min_x = min(top_left[0], bot_left[0])
        max_x = max(top_right[0], bot_right[0])
        min_y = min(top_left[1], top_right[1])
        max_y = max((bot_left[1]+30), (bot_right[1]+30))

        #define region of interest (crop are)
        x, y = min_x, min_y
        w, h = max_x - min_x, max_y - min_y
        roi = img[y:y+h, x:x+w]

        #perform crop
        cropped_image = roi.copy()
    return(cropped_image)

#a function to get the centre of a single contour, used by only the getContours function
def getCentre(contour):
    #calculate moments
    moments = cv2.moments(contour)

    #if the there are contours present
    if moments['m00'] != 0:
        #calculate x of the center point using:
        #centroid_x = Mx / M, where Mx is the sum of x and M is area
        x_centre = int(moments['m10'] / moments['m00'])

        #repeats same process for y
        y_centre = int(moments['m01'] / moments['m00'])
        return x_centre, y_centre
    else:
        return None

def getDotContours(img, img_contour):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt_count = 0
    cnt_centre_array = []
    #working out area to remove noise/ unwanted contours
    for cnt in contours:
        cnt_count = cnt_count + 1
        cnt_centre_array.append(getCentre(cnt))

    print(cnt_count, "Dot Contours(s) found at:", cnt_centre_array)
    print(cnt_centre_array)
    return(cnt_centre_array)
       
def dotMask(img):
    #'dotMask' is a function that takes in an image, applies a mask bespokely made for the aim point
    #create a red colour mask, capturing a range of red shades
    lower_mask = np.array([40, 50, 100], dtype = "uint8")
    upper_mask= np.array([65, 70, 250], dtype = "uint8")

    mask = cv2.inRange(img, lower_mask, upper_mask)

    masked_img = cv2.bitwise_and(img, img, mask = mask)

    return masked_img