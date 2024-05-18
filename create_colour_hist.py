import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

## This script creates a colour histogram of each colourspace shift, as a justification for using CMY over any other colourspace


# Paths and corresponding names
paths = [
    "colour_spaces/RGB.png",
    "colour_spaces/cmy_image.jpg",
    "colour_spaces/grey.jpg",
    "colour_spaces/HLS.jpg",
    "colour_spaces/HSV.jpg",
    "colour_spaces/YCR_CB.jpg",
    "colour_spaces/YCrCb.jpg",
    "colour_spaces/YUV.jpg"
]
names = ["RGB","CMY", "Grey", "HLS", "HSV", "YCrCb (YCR_CB)", "YCrCb", "YUV"]

# Loop through each path and corresponding name
for path, name in zip(paths, names):
    # Load an image
    image = cv2.imread(path)
    if image is None:
        print(f"Failed to load image at {path}. Please check the file path.")
        continue

    # Convert image from BGR to RGB if not a greyscale image
    # if len(image.shape) == 3:  # Checking if the image has three channels
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Determine number of channels
    num_channels = 1 if len(image.shape) == 2 else 3

    # Initialize the color list and labels for RGB or greyscale
    colors = ('r', 'g', 'b') if num_channels == 3 else ('black',)
    channel_labels = ('Red Channel', 'Green Channel', 'Blue Channel') if num_channels == 3 else ('Intensity',)

    plt.figure()
    # Create histograms for each color channel
    for i in range(num_channels):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.fill_between(range(256), hist.flatten(), color=colors[i], alpha=0.5, label=channel_labels[i])

    # Customize plot settings
    plt.xlim([0, 256])
    plt.title(f"{name} Color Histogram")
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.legend(loc='upper right')

    # Save the plot
    output_path = os.path.join("colour_spaces_histograms", f"{name.lower()}_histogram.png")
    plt.savefig(output_path)
    plt.close()
    print(f"Saved histogram to {output_path}")

