import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import os

# Ensure the output directory exists
output_dir = 'colour_space_histograms'
os.makedirs(output_dir, exist_ok=True)

# Paths and corresponding names
paths = [
    "colour_spaces/RGB.png"
    "colour_spaces/cmyimage.jpg",
    "colour_spaces/grey.jpg",
    "colour_spaces/HLS.jpg",
    "colour_spaces/HSV.jpg",
    "colour_spaces/YCR_CB.jpg",
    "colour_spaces/YCrCb.jpg",
    "colour_spaces/YUV.jpg"
]
names = ["RGB","CMY", "Grey", "HLS", "HSV", "YCrCb (YCR_CB)", "YCrCb", "YUV"]

def blend_colors(colors):
    result = np.array([1, 1, 1])
    for color in colors:
        rgb = np.array(mcolors.to_rgb(color))
        result = result * (1 - 0.5) + rgb * 0.5
    return result

for path, name in zip(paths, names):
    image = cv2.imread(path)
    if image is None:
        print(f"Failed to load image at {path}. Please check the file path.")
        continue

    #convert image from BGR to RGB if not a greyscale image
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    #determine number of channels
    num_channels = 1 if len(image.shape) == 2 else 3

    plt.figure(figsize=(10, 5))
    histograms = []
    colors = ['red', 'green', 'blue'] if num_channels == 3 else ['black']

    #create histograms for each color channel
    for i in range(num_channels):
        hist = cv2.calcHist([image], [i], None, [256], [0, 256]).flatten()
        histograms.append(hist)

    #plot combined histogram
    for i in range(256):
        slice_colors = [colors[j] for j, h in enumerate(histograms) if h[i] > 0]
        color = blend_colors(slice_colors) if slice_colors else [1, 1, 1]
        plt.fill_between([i, i+1], 0, max(h[i] for h in histograms), color=color, edgecolor='none')

    plt.xlim([0, 256])
    plt.title(f"{name} Combined Color Histogram")
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(output_dir, f"{name.lower()}_combined_histogram.png"))
    plt.close()
    print(f"Saved combined histogram to {output_dir}/{name.lower()}_combined_histogram.png")
