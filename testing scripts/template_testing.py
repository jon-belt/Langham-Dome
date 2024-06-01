import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, reticuleMask, getDotContours, getReticuleContours

def find_top_matches_and_percentiles(result_matrix):
    # Flatten the matrix and sort it
    flat = result_matrix.flatten()
    sorted_indices = np.argsort(flat)[::-1]  # Indices of elements in descending order

    # Calculate the indices for the required percentiles (1st to 10th) and max
    percentiles = [0.01, 0.02, 0.03, 0.04, 0.06, 0.07, 0.08, 0.09, 0.10, 0.99]  # Changed the last percentile to 0.99
    percentile_indices = [int(len(sorted_indices) * p) for p in percentiles]
    percentile_indices = [min(idx, len(sorted_indices) - 1) for idx in percentile_indices]  # Ensure indices are within bounds

    # List to store the value and location for each percentile
    matches = []

    for idx in percentile_indices:
        # Get the flattened index for the percentile
        flat_index = sorted_indices[idx]
        # Convert the flattened index to 2D index
        match_loc = np.unravel_index(flat_index, result_matrix.shape)
        # Get the match value
        match_val = result_matrix[match_loc]
        # Store the value and location (as x, y)
        matches.append((match_val, (match_loc[1], match_loc[0])))

    return matches

reticule_path = ("./imgs/reticule.png")
reticule_dot_path = ("./imgs/reticuleAndDot.png")
dot_path = ("./imgs/dot.png")
three_dot_path = ("./imgs/3dots.png")
three_dot_path2 = ("./imgs/3dots2.png")
good_score = ("./imgs/bad_score.png")
bad_score = ("./imgs/good_score.png")

#load in current frame & make copy
img1 = cv2.imread(three_dot_path)
img2 = cv2.imread(three_dot_path2)
img3 = cv2.imread(reticule_path)
img4 = cv2.imread(reticule_dot_path)
img5 = cv2.imread(good_score)
img6 = cv2.imread(bad_score)

#imgs = [img1, img2, img3, img4, img5, img6]
imgs = [img5]

#load in template, convert to cmy, then convert to greyscale
ret = cv2.imread("./templates/bottomArch2.png")
#ret_cmy = cmyConversion(ret)
template = cv2.cvtColor(ret, cv2.COLOR_BGR2GRAY)

#find height and width for template
h, w = template.shape

#find best method
methods = [cv2.TM_CCOEFF]

count = 1

for img in imgs:
    img = cmyConversion(img)
    img = reticuleMask(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, cv2.TM_CCORR)

    # #sets min and max location
    # min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


    top_matches = find_top_matches_and_percentiles(result)

    # Draw rectangles for each match in the top_matches
    for i, (match_val, match_loc) in enumerate(top_matches):
        print(f"Percentile {10 - i if i < 9 else 'Max'}: Value = {match_val}, Location = {match_loc}")

        # Calculate the bottom right corner of the rectangle
        bottom_right = (match_loc[0] + w, match_loc[1] + h)

        # Set a unique color for each rectangle
        # For illustration, I'm varying the blue component of the color
        color = (255, 0, 255 - i * 25)  # Decrease blue component with each rectangle

        # Draw the rectangle
        cv2.rectangle(img2, match_loc, bottom_right, color, 2)

    # Display the image with the drawn rectangles
    cv2.imshow(str(count), img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    count = count + 1