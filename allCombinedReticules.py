import cv2
import numpy as np
from transformations import dotMask, getDotContours, crop, cmyConversion

def locateReticule(imagePath, param1_list, param2_list, *color_spaces):
    print("locateReticule Called")
    img = cv2.imread(imagePath)
    cropped = crop(img)  # crops img to size of projection

    centers = []
    radii = []

    for color_space in color_spaces:
        if len(img.shape) == 2 or img.shape[2] == 1:  # Image is already grayscale
            shiftedImg = cropped
        elif color_space == 'Greyscale':
            shiftedImg = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
        elif color_space == 'HLS':
            shiftedImg = cv2.cvtColor(cropped, cv2.COLOR_BGR2HLS)
        elif color_space == 'HSV':
            shiftedImg = cv2.cvtColor(cropped, cv2.COLOR_BGR2HSV)
        elif color_space == 'YUV':
            shiftedImg = cv2.cvtColor(cropped, cv2.COLOR_BGR2YUV)
        elif color_space == 'YCrCb':
            shiftedImg = cv2.cvtColor(cropped, cv2.COLOR_BGR2YCrCb)
        elif color_space == 'CMY':
            shiftedImg = cmyConversion(cropped)
        else:
            shiftedImg = cropped

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
        output_path = f"testing_images1/final_average.png"
        cv2.imwrite(output_path, cropped)
        print(f"Saved final image with averaged circle to {output_path}")
    else:
        print("No circles found")

image_path = 'imgs/good_score.png'
#image_path = 'imgs/bad_score.png'
#image_path = 'imgs/reticule.png'
param1_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
param2_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

locateReticule(image_path, param1_list, param2_list, 'CMY', 'HLS', 'HSV', 'YUV', 'YCrCb', 'RGB')
