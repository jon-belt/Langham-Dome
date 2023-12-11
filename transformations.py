#this script holds all image transformation functions
import cv2
import numpy as np

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

def getContours(img, img_contour):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt_count = 0
    cnt_centre_array = []
    #working out area to remove noise/ unwanted contours
    for cnt in contours:
        cnt_count = cnt_count + 1
        cnt_centre_array.append(getCentre(cnt))

    print(cnt_count, "Dot(s) found.")
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

def reticuleMask(img):
    #'reticuleMask' is a function that takes in an image, applies a mask bespokely made for the reticule
    #create a deep purple colour mask, capturing a range of red shades
    lower_mask = np.array([40, 50, 100], dtype = "uint8")
    upper_mask= np.array([65, 70, 250], dtype = "uint8")

    mask = cv2.inRange(img, lower_mask, upper_mask)

    masked_img = cv2.bitwise_and(img, img, mask = mask)

    return masked_img