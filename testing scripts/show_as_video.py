from transformations import cmyConversion, dotMask
import numpy as np
import cv2

cap = cv2.VideoCapture('videos/5.mp4') 
if not cap.isOpened():
    print("Error: Couldn't open the video file.")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cmyImg = cmyConversion(frame)
    result = dotMask(cmyImg)

    out.write(result)

    cv2.imshow('CMY Conversion', result)

    if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()