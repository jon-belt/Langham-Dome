import cv2
import numpy as np
from transformations import dotMask, getDotContours, crop, cmyConversion

def locateDot(imagePath):
    print("locateDot Called")
    img = cv2.imread(imagePath)
    if img is not None:
        img = cv2.imread(imagePath)     #reads in img
        img = crop(img)                 #crops img to size of projection
        img_contour = img.copy()        #creates a copy for contours
        img_cmy = cmyConversion(img)    #converts to cmy
        img_dots = dotMask(img_cmy)     #applies mask to find dots
        img_dots_blur = cv2.GaussianBlur(img_dots, (7, 7), 1)               #blur to help preprocessing
        img_dots_grey = cv2.cvtColor(img_dots_blur, cv2.COLOR_BGR2GRAY)     #converts to greyscale

        img_canny = cv2.Canny(img_dots_grey, 150, 225)      #uses canny edge finder with 150, 225 as parameters

        #help reduce noise
        kernel = np.ones((5,5))
        img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

        #runs get contours function and populates 'img_contour'
        return getDotContours(img_dilate, img_contour)
    else:
        print("Error: Unable to load the image.")
        return(-1)

# def locateReticule(imagePath):
#     print("locateReticule Called")
#     img = cv2.imread(imagePath)
#     cropped = crop(img)         #crops img to size of projection

#     cv2.imshow("cropped", cropped)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)    #convert to grayscale

#     gray_blurred = cv2.GaussianBlur(gray, (1, 1), 0)    #apply blur to reduce noise

#     #apply hough circle transform
    
#     ### change this depending on the resolution !!!
#     circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 440, param1=10, param2=5, minRadius=int(410/2), maxRadius=int(440/2))

#     #find list of circles, get first one
#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         first_circle = circles[0, 0]                    #get first circle
#         center = (first_circle[0], first_circle[1])     #get centre of circle
#         print("Reticule Found at:", center)
#         return center

def locateReticule(imagePath):
    print("locateReticule Called")
    img = cv2.imread(imagePath)
    cropped = crop(img)  # crops img to size of projection

    cmy = cmyConversion(cropped)

    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)  # convert to grayscale
    gray_blurred = cv2.GaussianBlur(gray, (1, 1), 0)  # apply blur to reduce noise

    # apply hough circle transform
    # change this depending on the resolution
    circles = cv2.HoughCircles(
        gray_blurred, cv2.HOUGH_GRADIENT, 1, 440, param1=10, param2=5, minRadius=int(410 / 2), maxRadius=int(440 / 2)
    )

    # find list of circles, get first one
    if circles is not None:
        circles = np.uint16(np.around(circles))
        first_circle = circles[0, 0]  # get first circle
        center = (first_circle[0], first_circle[1])  # get centre of circle
        radius = first_circle[2]  # get radius of circle
        print("Reticule Found at:", center)

        # draw the circle and its center
        cv2.circle(cmy, center, radius, (0, 255, 0), 2)  # draw the circle
        cv2.circle(cmy, center, 1, (0, 0, 255), 3)  # draw the center of the circle

        # display the image with the circle
        cv2.imshow("Detected Reticule", cmy)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return center