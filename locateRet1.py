from calculations import calcScore
from highscores import HighScores
import tkinter as tk
from tkinter import Toplevel, Label, Entry, Radiobutton, IntVar, Button
from transformations import crop
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import time

def expand_edges(image):
    hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    gray = cv2.cvtColor(hls, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    edges = cv2.Canny(blurred, 14, 16)
    dilated_edges = cv2.dilate(edges, None, iterations=10)
    blurred_dilated_edges = cv2.GaussianBlur(dilated_edges, (5, 5), 0)
    
    return blurred_dilated_edges

def locateDot1(image_path):
    param1_list = [10]
    param2_list = [1, 3, 4, 5, 6, 7, 8]
    
    testImg = crop(cv2.imread(image_path))
    expanded = expand_edges(testImg)
    best_circle = None
    min_distance = float('inf')
    best_params = None
    
    for param1 in param1_list:
        for param2 in param2_list:
            circles = cv2.HoughCircles(expanded, cv2.HOUGH_GRADIENT, 1, 440, param1=param1, param2=param2,
                                       minRadius=int(410 / 2), maxRadius=int(440 / 2))
            
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for circle in circles[0, :]:
                    center = (circle[0], circle[1])
                    distance = calculate_distance(center, real_coord)
                    if distance < min_distance:
                        min_distance = distance
                        best_circle = center
                        best_params = (param1, param2)
    
    return best_circle, best_params, min_distance

def calculate_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

image_paths = [f'imgs/ret/{i}_cropped.png' for i in range(1, 11)]
real_coords_list = [
    (472, 410), (212, 266), (455, 333), (616, 340), (491, 326),
    (536, 419), (466, 445), (594, 354), (548, 296), (492, 331)
]

for image_path, real_coord in zip(image_paths, real_coords_list):
    start_time = time.time()
    detected_center, best_params, min_distance = locateDot1(image_path)
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    if detected_center:
        print(f"Image: {image_path}, Detected Center: {detected_center}, Real Coord: {real_coord}, "
              f"Best Params: {best_params}, Min Distance: {min_distance:.2f}, Time: {elapsed_time:.4f} seconds")
    else:
        print(f"No circles detected in image: {image_path}, Time: {elapsed_time:.4f} seconds")

cv2.imshow("img", expand_edges(crop(cv2.imread(image_paths[0]))))
cv2.waitKey(0)
cv2.destroyAllWindows()
