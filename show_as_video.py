from conversions import cmyConversion
import numpy as np
import cv2

cyan = 20
magenta = 88
yellow = 118

#opens file with error checking
cap = cv2.VideoCapture('videos/6.mp4') 
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

# Get the video properties
fps = cap.get(cv2.CAP_PROP_FPS)

while True:
    ret, frame = cap.read()
    #breaks loop when video ends
    if not ret:
        break
    #convert each frame to CMY
    conversion = cmyConversion(frame)

    #creates mask
    red_mask = (conversion[1] > cyan) & (conversion[2] < magenta) & (conversion[3] > yellow)

    result = np.zeros_like(conversion[0])
    result[red_mask] = conversion[0][red_mask]

    cv2.imshow('CMY Conversion', result)  #access CMY image through cmy_result[0]

    #shut video if 'q' pressed
    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()