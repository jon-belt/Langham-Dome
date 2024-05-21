import cv2
import numpy as np
from transformations import cmyConversion

# load in the dots, cropped
left_dot_image = cv2.imread('imgs/second/left.png')
right_dot_image = cv2.imread('imgs/second/right.png')
middle_dot_image = cv2.imread('imgs/second/middle.png')

# get pixel value at a coordinate
def get_pixel_value(image, coords):
    return image[coords[1], coords[0]]

# converts to every colourspace im using
def convert_and_get_pixel_values(image, coords1, coords2):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    cmy_image = cmyConversion(image)
    
    # get the values at the dot centre (50,50) and the background (25, 50), both determined 
    pixel_values = {
        'RGB': (get_pixel_value(image, coords1), get_pixel_value(image, coords2)),
        'Grayscale': (get_pixel_value(gray_image, coords1), get_pixel_value(gray_image, coords2)),
        'HLS': (get_pixel_value(hls_image, coords1), get_pixel_value(hls_image, coords2)),
        'CMY': (get_pixel_value(cmy_image, coords1), get_pixel_value(cmy_image, coords2)),
        'HSV': (get_pixel_value(hsv_image, coords1), get_pixel_value(hsv_image, coords2)),
        'YCrCb': (get_pixel_value(ycrcb_image, coords1), get_pixel_value(ycrcb_image, coords2)),
        'YUV': (get_pixel_value(yuv_image, coords1), get_pixel_value(yuv_image, coords2))
    }

    return pixel_values

# calculate contrast ratio with (L1 + 0.05)/(L2 + 0.05)
def calculate_contrast_ratio(color1, color2):
    L1 = np.mean(color1) / 255.0
    L2 = np.mean(color2) / 255.0
    contrast_ratio = (L1 + 0.05) / (L2 + 0.05)
    return contrast_ratio

# coordinates arent hard coded incase i want to change this algorithm
aim_point_coords = (50, 50)
background_coords = (25, 50)

### left dot
left_dot_pixel_values = convert_and_get_pixel_values(left_dot_image, aim_point_coords, background_coords)

### right dot
right_dot_pixel_values = convert_and_get_pixel_values(right_dot_image, aim_point_coords, background_coords)

### middle dot
middle_dot_pixel_values = convert_and_get_pixel_values(middle_dot_image, aim_point_coords, background_coords)

print("Left Dot Contrast Ratios:")
for space, (color1, color2) in left_dot_pixel_values.items():
    ratio = calculate_contrast_ratio(color1, color2)
    print(f"{space} Contrast Ratio: {ratio}")

print("\nRight Dot Contrast Ratios:")
for space, (color1, color2) in right_dot_pixel_values.items():
    ratio = calculate_contrast_ratio(color1, color2)
    print(f"{space} Contrast Ratio: {ratio}")

print("\nMiddle Dot Contrast Ratios:")
for space, (color1, color2) in middle_dot_pixel_values.items():
    ratio = calculate_contrast_ratio(color1, color2)
    print(f"{space} Contrast Ratio: {ratio}")
