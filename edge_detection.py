import cv2
import numpy as np
import matplotlib.pyplot as plt
from transformations import cmyConversion
import time

def percentage_grey(img):
    non_black_pixels = np.count_nonzero(img)
    total_pixels = img.shape[0] * img.shape[1]
    percentage = (non_black_pixels / total_pixels) * 100
    return percentage

def edge_detection(image, color_space, param1, param2):
    if len(image.shape) == 2 or image.shape[2] == 1:  # Image is already grayscale
        converted_image = image
    elif color_space == 'Grayscale':
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif color_space == 'HLS':
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
    elif color_space == 'HSV':
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    elif color_space == 'YUV':
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
    elif color_space == 'YCrCb':
        converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    elif color_space == 'CMY':
        converted_image = cmyConversion(image)
    else:
        converted_image = image
    
    edges = cv2.Canny(converted_image, param1, param2)
    return edges, converted_image

def process_image(image_path, param1, param2):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image at {image_path}. Please check the file path.")
        return None

    color_spaces = ['RGB', 'Grayscale', 'HLS', 'HSV', 'YUV', 'YCrCb', 'CMY']
    grey_percentages = {}

    for color_space in color_spaces:
        edges, converted_image = edge_detection(image, color_space, param1, param2)
        grey_percentage = percentage_grey(edges)  # Use edges to calculate grey percentage
        grey_percentages[color_space] = grey_percentage
        print(f"Grey percentage in {color_space} (Lower: {param1}, Upper: {param2}): {grey_percentage:.2f}%")
    
    return grey_percentages

img1 = 'imgs/reticule.png'
img2 = 'imgs/good_score.png'

lowerBound = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]
upperBound = 10

results = {color_space: [] for color_space in ['RGB', 'Grayscale', 'HLS', 'HSV', 'YUV', 'YCrCb', 'CMY']}

for lb in lowerBound:
    grey_percentages = process_image(img1, lb, upperBound)
    if grey_percentages:
        for color_space, grey_percentage in grey_percentages.items():
            results[color_space].append((lb, grey_percentage))

# Plot the results
plt.figure(figsize=(10, 6))
for color_space, values in results.items():
    x, y = zip(*values)
    plt.plot(x, y, label=color_space)

plt.xlabel('Lower Threshold')
plt.ylabel('Grey Percentage')
plt.title('Grey Percentage vs. Lower Threshold for Different Color Spaces')
plt.legend()
plt.show()