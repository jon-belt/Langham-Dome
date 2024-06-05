from transformations import crop
import cv2

image_paths = [f'imgs/ret/{i}.png' for i in range(1, 11)]

for i, image_path in enumerate(image_paths, 1):
    img = cv2.imread(image_path)
    cropped = crop(img)
    cv2.imwrite(f'imgs/ret/{i}_cropped.png', cropped)

