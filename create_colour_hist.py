import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from transformations import cmyConversion

## This script creates a colour histogram of each colourspace shift, as a justification for using CMY over any other colourspace

def create_histogram(image, color_space, save_path):
    """Create and save a color histogram for an image in a given color space."""
    num_channels = 1 if len(image.shape) == 2 else 3
    colors = ('r', 'g', 'b') if num_channels == 3 else ('black',)
    channel_labels = ('Red Channel', 'Green Channel', 'Blue Channel') if num_channels == 3 else ('Intensity',)

    plt.figure()
    for i in range(num_channels):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.fill_between(range(256), hist.flatten(), color=colors[i], alpha=0.5, label=channel_labels[i])

    plt.xlim([0, 256])
    plt.title(f"{color_space} Color Histogram for the Right Aim Point")
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    plt.savefig(save_path)
    plt.close()

def process_image(image_path, output_dir):
    """Process an image, convert it to various color spaces, and create histograms."""
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image at {image_path}. Please check the file path.")
        return

    color_spaces = {
        'RGB': image,
        'Grayscale': cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
        'HLS': cv2.cvtColor(image, cv2.COLOR_BGR2HLS),
        'HSV': cv2.cvtColor(image, cv2.COLOR_BGR2HSV),
        'YUV': cv2.cvtColor(image, cv2.COLOR_BGR2YUV),
        'YCrCb': cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb),
        'CMY': cmyConversion(image)
    }

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for color_space, converted_image in color_spaces.items():
        save_path = os.path.join(output_dir, f"{color_space.lower()}_histogram.png")
        create_histogram(converted_image, color_space, save_path)
        print(f"Saved {color_space} histogram to {save_path}")

image_path = 'imgs/testing images/aim point justification/first testing img/rightDot.png'
output_dir = 'colour_spaces_histograms'
process_image(image_path, output_dir)
