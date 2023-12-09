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
    img_and_channels = [cmy_img, cyan_channel, magenta_channel, yellow_channel]

    #any code using this function can access the image variable through x[0], and the channels through x[1,2,3] (cyan, magenta, yellow)
    return(img_and_channels)