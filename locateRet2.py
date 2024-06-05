import cv2
import numpy as np
import time
from transformations import dotMask, getDotContours, crop, cmyConversion

def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def locateReticule(imagePath):
    print(f"Processing {imagePath}")
    img = cv2.imread(imagePath)
    cropped = crop(img)  # crops img to size of projection

    centers = []
    radii = []

    color_spaces = ['HLS', 'CMY']  # Only HLS and CMY
    param1_list = [10,11,12,13,14,15,16,17,18,19,20,21]
    param2_list = [1,2,3,4,5,6,7,8,9,10,11]

    for color_space in color_spaces:
        if color_space == 'HLS':
            shiftedImg = cv2.cvtColor(cropped, cv2.COLOR_BGR2HLS)
        elif color_space == 'CMY':
            shiftedImg = cmyConversion(cropped)

        gray = cv2.cvtColor(shiftedImg, cv2.COLOR_BGR2GRAY)  # convert to grayscale
        gray_blurred = cv2.GaussianBlur(gray, (1, 1), 0)  # apply blur to reduce noise

        for param1 in param1_list:
            for param2 in param2_list:
                # apply hough circle transform
                circles = cv2.HoughCircles(
                    gray_blurred, cv2.HOUGH_GRADIENT, 1, 440, param1=param1, param2=param2,
                    minRadius=int(410 / 2), maxRadius=int(440 / 2)
                )

                if circles is not None:
                    circles = np.uint16(np.around(circles))
                    first_circle = circles[0, 0]  # get first circle
                    center = (first_circle[0], first_circle[1])  # get centre of circle
                    radius = first_circle[2]  # get radius of circle
                    centers.append(center)
                    radii.append(radius)

    if centers:
        avg_center = np.mean(centers, axis=0).astype(int)
        avg_radius = int(np.mean(radii))

        # draw the circle and its center on the original image
        cv2.circle(cropped, tuple(avg_center), avg_radius, (0, 255, 0), 2)  # draw the circle
        cv2.circle(cropped, tuple(avg_center), 1, (0, 0, 255), 3)  # draw the center of the circle

        # save the image with the final circle
        output_path = f"testing_images1/final_average_{imagePath.split('/')[-1]}"
        cv2.imwrite(output_path, cropped)
        
        return tuple(avg_center)
    else:
        print("No circles found")
        return None

def calculate_distance(coords, reticule_center):
    if reticule_center is not None:
        distance = euclidean_distance(coords, reticule_center)
        return distance
    else:
        return None

# Example coordinates for each image
real_coords_list = [
    (472, 410), (212, 266), (455, 333), (616, 340), (491, 326),
    (536, 419), (466, 445), (594, 354), (548, 296), (492, 331)
]

image_paths = [f'imgs/ret/{i}_cropped.png' for i in range(1, 11)]

for idx, image_path in enumerate(image_paths):
    real_coords = real_coords_list[idx]
    start_time = time.time()
    reticule_center = locateReticule(image_path)
    end_time = time.time()
    distance = calculate_distance(real_coords, reticule_center)
    elapsed_time = end_time - start_time
    print(f"Image {idx+1}: Distance from real coordinates {real_coords} to detected center: {distance:.2f}. Seconds (Time taken: {elapsed_time:.2f}s)" if distance is not None else f"Image {idx+1}: No reticule center found (Time taken: {elapsed_time:.2f}s)")
