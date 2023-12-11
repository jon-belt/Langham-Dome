import cv2
import numpy as np
from conversions import cmyConversion
from stack_images import stackImages
from masks import dotMask

def locateDot(imagePath):
    img = cv2.imread(imagePath)
    if img is not None:
        cmy_img = cmyConversion(img)
        masked_img = dotMask(cmy_img)
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


