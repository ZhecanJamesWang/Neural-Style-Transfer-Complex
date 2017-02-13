import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('images/inputs/face/style/CFD-BM-033-003-N_2048FC.png',1)
# resizedImage = cv2.resize(img, (400, 400))
croppedImage = img[500:1520, 570:1480]
cv2.imshow('image', croppedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('cropped_CFD-BM-033-003-N_2048FC.png',croppedImage)

