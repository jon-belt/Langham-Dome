import cv2
import numpy as np
from conversions import cmyConversion
from stack_images import stackImages
from masks import dotMask

frame_width = 64
frame_height = 48
cap = cv2.VideoCapture('videos/6trimmed.mp4')
cap.set(3, frame_width)
cap.set(4, frame_height)

while True:
    sucess, img = cap.read()
    img_cmy = cmyConversion(img)
    img_dots = dotMask(img_cmy)
    img_dots_blur = cv2.GaussianBlur(img_dots, (7, 7), 1)
    img_dots_grey = cv2.cvtColor(img_dots_blur, cv2.COLOR_BGR2GRAY)

    img_stack = stackImages(0.33, ([img_dots, img_dots_blur, img_dots_grey]))

    cv2.imshow("Result", img_stack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
