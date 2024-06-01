import cv2
import numpy as np
from conversions import cmyConversion
from stack_images import stackImages
from transformations import dotMask

three_dot_path = ("./imgs/3dots.png")
frame_width = 64
frame_height = 48
cap = cv2.VideoCapture('videos/6trimmed2.mp4')
cap.set(3, frame_width)
cap.set(4, frame_height)

def empty(a):
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 150, 225, empty)
cv2.createTrackbar("Threshold2", "Parameters", 150, 225, empty)

cont_list = []

#a function to get the centre of a single contour
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
        area = cv2.contourArea(cnt)
        #only draws contours above a certain size
        # if area >= (1): #currently draws all contours as i might remove this in the future
        cnt_centre_array.append(getCentre(cnt))

    print(cnt_count, "Contour(s) found.")
    print(cnt_centre_array)
    return(cnt_centre_array)


while True:
    sucess, img = cap.read()
    img = cv2.imread(three_dot_path)
    img_contour = img.copy()

    #reads every frame in, performs CMY conversion and applies the mask for the dots
    img_cmy = cmyConversion(img)
    img_dots = dotMask(img_cmy)
    img_dots_blur = cv2.GaussianBlur(img_dots, (7, 7), 1)
    img_dots_grey = cv2.cvtColor(img_dots_blur, cv2.COLOR_BGR2GRAY)

    #threshold trackbars, so i can scale up the contours and find the specific values that work
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    img_canny = cv2.Canny(img_dots_grey, threshold1, threshold2)

    #help reduce noise
    kernel = np.ones((1,1))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

    #runs get contours function and populates 'img_contour'
    getContours(img_dilate, img_contour)

    img_stack = stackImages(0.4, ([img_cmy, img_dots],
                                   [img_dilate, img_contour]))

    cv2.imshow("Result", img_stack)
    break
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
        break
