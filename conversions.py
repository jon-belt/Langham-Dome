###  This script holds function(s) that convert from BGR colour space to unique colour spaces OpenCV doesnt provide

import cv2

def cmyConversion(img):
    #split channels for CMY conversion
    blue_channel, green_channel, red_channel = cv2.split(img)

    #calculate the CMY channels
    cyan_channel = 1 - red_channel
    magenta_channel = 1 - green_channel
    yellow_channel = 1 - blue_channel

    #merge the CMY channels into a single image
    cmy_img = cv2.merge((cyan_channel, magenta_channel, yellow_channel))
    return(cmy_img)