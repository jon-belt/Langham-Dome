import cv2
import numpy as np
from conversions import cmyConversion
from stack_images import stackImages
from transformations import dotMask

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

while True:
    sucess, img = cap.read()

    #reads every frame in, performs CMY conversion and applies the mask for the dots
    img_cmy = cmyConversion(img)
    img_dots = dotMask(img_cmy)
    img_dots_blur = cv2.GaussianBlur(img_dots, (7, 7), 1)
    img_dots_grey = cv2.cvtColor(img_dots_blur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    img_canny = cv2.Canny(img_dots_grey, threshold1, threshold2)

    #img_stack = stackImages(0.8, ([img_canny]))

    result_img = cv2.resize(img_canny, (1600, 800))
    cv2.imshow("Result", result_img)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
        break
