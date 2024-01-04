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

def getDotContours(img, img_contour):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt_count = 0
    cnt_centre_array = []
    #working out area to remove noise/ unwanted contours
    for cnt in contours:
        cnt_count = cnt_count + 1
        cnt_centre_array.append(getCentre(cnt))

    print(cnt_count, "Dot Contours(s) found.")
    print(cnt_centre_array)
    return(cnt_centre_array)

def getReticuleContours(img, img_contour):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt_count = 0
    #working out area to remove noise/ unwanted contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #only draws contours above a certain size
        if area >= (1000):
            cv2.drawContours(img_contour, cnt, -1, (255, 0 ,255), 7)
            cnt_count = cnt_count + 1
            y_offset = (525-397)
            contour_centre = getCentre(cnt)
            reticule_x = contour_centre[0]
            reticule_y = (contour_centre[1]+y_offset)
            #may need to return touple of array and contour no. if algorithm detects multiple reticule contours on different test videos
        else:
            print("No reticule found.")
        
        if cnt_count == 0:
            print(cnt_count, "Reticule Contour(s) found.")
            return(None)
        else:
            print(cnt_count, "Reticule Contour(s) found.")
            reticule_centre = [reticule_x, reticule_y]
            #print(reticule_centre)
            return([reticule_x, reticule_y])
            
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
                          # B   G   R
    lower_mask = np.array([39, 16, 25], dtype = "uint8")
    upper_mask= np.array([61, 32, 62], dtype = "uint8")

    mask = cv2.inRange(img, lower_mask, upper_mask)

    masked_img = cv2.bitwise_and(img, img, mask = mask)

    return masked_img