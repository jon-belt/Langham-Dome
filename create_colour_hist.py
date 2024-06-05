import cv2
import matplotlib.pyplot as plt
import os
from transformations import cmyConversion

# Function to compute and normalize histogram
def compute_histogram(image, channel):
    hist = cv2.calcHist([image], [channel], None, [256], [0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def create_histogram(image, color_space, save_path, y_max):
    channelNum = 1 if len(image.shape) == 2 else image.shape[2]
    if channelNum == 4:
        colors = ('r', 'g', 'b', 'a')
        channel_labels = ('Red Channel', 'Green Channel', 'Blue Channel', 'Alpha Channel')
    elif channelNum == 3:
        colors = ('r', 'g', 'b')
        channel_labels = ('Red Channel', 'Green Channel', 'Blue Channel')
    else:
        colors = ('black',)
        channel_labels = ('Intensity',)

    plt.figure()
    for i in range(channelNum):
        hist = compute_histogram(image, i)
        plt.fill_between(range(256), hist, color=colors[i], alpha=0.5, label=channel_labels[i])

    plt.xlim([0, 256])
    plt.ylim([0, y_max])
    plt.title(f"{color_space} Color Histogram")
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')
    plt.savefig(save_path)
    plt.close()

def process_image(image_path, output_dir, y_max):
    image = cv2.imread(image_path)
    if image is None:
        return

    # Define color spaces
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

    # Create and save histograms with normalized y-axis
    for color_space, converted_image in color_spaces.items():
        save_path = os.path.join(output_dir, f"{color_space.lower()}_histogram.png")
        create_histogram(converted_image, color_space, save_path, y_max)
        print(f"Saved {color_space}")

# Calculate max frequency across all images for normalization
def calculate_max_frequency(image_paths):
    max_freq = 0
    for image_path in image_paths:
        image = cv2.imread(image_path)
        if image is None:
            continue

        # Define color spaces
        color_spaces = {
            'RGB': image,
            'Grayscale': cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
            'HLS': cv2.cvtColor(image, cv2.COLOR_BGR2HLS),
            'HSV': cv2.cvtColor(image, cv2.COLOR_BGR2HSV),
            'YUV': cv2.cvtColor(image, cv2.COLOR_BGR2YUV),
            'YCrCb': cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb),
            'CMY': cmyConversion(image)
        }

        # Compute maximum y value for normalization
        for color_space, converted_image in color_spaces.items():
            channelNum = 1 if len(converted_image.shape) == 2 else 3
            for i in range(channelNum):
                hist = compute_histogram(converted_image, i)
                max_freq = max(max_freq, hist.max())

    return max_freq

left = 'imgs/leftDot1.png'
right = 'imgs/rightDot1.png'
both = 'imgs/testing images/aim points white.png'
og = 'imgs/testing images/rgb.png'

left_output_dir = 'histograms/L_Histograms'
right_output_dir = 'histograms/R_Histograms'
both_output_dir = 'histograms/LR_Histograms'
og_output_dir = 'histograms'

# Calculate the maximum frequency for normalization
image_paths = [left, right, og]
y_max = calculate_max_frequency(image_paths)

# Process each image
process_image(left, left_output_dir, y_max)
process_image(right, right_output_dir, y_max)
process_image(both, both_output_dir, y_max)
process_image(og, og_output_dir, y_max)
