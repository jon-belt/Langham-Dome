import cv2
import numpy as np
from conversions import cmyConversion
from transformations import dotMask, getCentre, getContours

def locateDot(imagePath):
    img = cv2.imread(imagePath)
    if img is not None:
        img = cv2.imread(imagePath)
        img_contour = img.copy()

        #reads in img, and performs transformations
        img_cmy = cmyConversion(img)
        img_dots = dotMask(img_cmy)
        img_dots_blur = cv2.GaussianBlur(img_dots, (7, 7), 1)
        img_dots_grey = cv2.cvtColor(img_dots_blur, cv2.COLOR_BGR2GRAY)

        img_canny = cv2.Canny(img_dots_grey, 150, 225)

        #help reduce noise
        kernel = np.ones((1,1))
        img_dilate = cv2.dilate(img_canny, kernel, iterations=1)

        #runs get contours function and populates 'img_contour'
        getContours(img_dilate, img_contour)
    else:
        print("Error: Unable to load the image.")








#OUT DATED BUT KEEPING FOR NOW
def locateDot1(imagePath):
    img = cv2.imread(imagePath)
    if img is not None:
        cmy_img = cmyConversion(img) 
        masked_img = dotMask(cmy_img)

        #converts to binary image, because there are still minute pixle differences in the red dot
        binary_image = cv2.cvtColor(masked_img, cv2.COLOR_BGR2GRAY)

        ### next section of code finds a single red dot, based on whbere the first non black pixel is - THIS DOES NOT WORK FOR MANY DOTS

        #find coordinates of non-zero pixels
        nonzero_coords = cv2.findNonZero(binary_image)

        #checks if there is a red dot
        if len(nonzero_coords) > 0:
            #sets first and last pixel
            x_coords = nonzero_coords[:, 0, 0]
            y_coords = nonzero_coords[:, 0, 1]

            center_x = np.round(np.mean(x_coords))
            center_y = np.round(np.mean(y_coords))

            dot_centre = [center_x, center_y]

            print(f"Dot Centre: {dot_centre}")
        else:
            print("No red dot found in the image.")
    else:
        print("Error: Unable to load the image.")


