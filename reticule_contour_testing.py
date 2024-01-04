import cv2
import numpy as np
from conversions import cmyConversion
from stack_images import stackImages
from transformations import reticuleMask, getReticuleContours

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
noisy_reticule = ("./imgs/noisy_reticule.png")
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

while True:
    sucess, img = cap.read()
    img = cv2.imread(reticule_dot_path)
    img_contour = img.copy()

    #reads every frame in, performs CMY conversion and applies the mask for the dots
    img_cmy = cmyConversion(img)
    img_reticule = reticuleMask(img_cmy)
    img_reticule_blur = cv2.GaussianBlur(img_reticule, (9, 9), 1)

    # img_path = ("test.png")
    # cv2.imwrite(img_path, img_reticule_blur)
    # cv2.imshow('Red Mask', result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    img_canny = cv2.Canny(img_reticule_blur, threshold1, threshold2)

    #help reduce noise
    kernel = np.ones((5,5))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

    #runs get contours function and populates 'img_contour'
    getReticuleContours(img_dilate, img_contour)

    img_stack = stackImages(0.25, ([img_reticule, img_canny],
                                   [img_dilate, img_contour]))

    cv2.imshow("Result", img_stack)
    if cv2.waitKey(1) & 0xFF == ord('q') or cv2.waitKey(1) & 0xFF == ord('Q'):
        break
