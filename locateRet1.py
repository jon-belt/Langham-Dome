from calculations import calcScore
from highscores import HighScores
import tkinter as tk
from tkinter import Toplevel, Label, Entry, Radiobutton, IntVar, Button
from transformations import crop
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def expand_edges(image):
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    gray = cv2.cvtColor(hls, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edges = cv2.Canny(blurred, 14, 16)
    dilated_edges = cv2.dilate(edges, None, iterations=10)
    blurred_dilated_edges = cv2.GaussianBlur(dilated_edges, (5, 5), 0)
    
    return blurred_dilated_edges

testImg1 = crop(cv2.imread("imgs/3dots.png"))
testImg2 = crop(cv2.imread("imgs/3dots2.png"))
testImg3 = crop(cv2.imread("imgs/bad_score.png"))
testImg4 = crop(cv2.imread("imgs/good_score.png"))
testImg5 = crop(cv2.imread("imgs/reticule.png"))
testImg6 = crop(cv2.imread("imgs/reticuleAndDot.png"))

param1_list = [10,11,12,13,14,15,16,17,18,19,20,21]
param2_list = [1,2,3,4,5,6,7,8,9,10,11]

expanded = expand_edges(testImg1)
for param1 in param1_list:
    for param2 in param2_list:
        circles = cv2.HoughCircles(expanded, cv2.HOUGH_GRADIENT, 1, 440, param1=param1, param2=param2,
                                   minRadius=int(410 / 2), maxRadius=int(440 / 2))
        
        if circles is not None:
            circles = np.uint16(np.around(circles))
            first_circle = circles[0, 0]  # Get the first circle

            img_with_circle = testImg1.copy()  # Copy the original image to draw the circle on
            
            # Draw the outer circle
            cv2.circle(img_with_circle, (first_circle[0], first_circle[1]), first_circle[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(img_with_circle, (first_circle[0], first_circle[1]), 2, (0, 0, 255), 3)
            
            output_path = f"testing_images1/{param1}_{param2}.png"
            cv2.imwrite(output_path, img_with_circle)
            print(f"Saved final image with averaged circle to {output_path}")
        else:
            print(f"No circles found for param1={param1} and param2={param2}")

cv2.imshow("img", expanded)
cv2.waitKey(0)

cv2.destroyAllWindows()

