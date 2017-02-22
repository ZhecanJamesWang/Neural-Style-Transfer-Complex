import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('images/inputs/face/style/cropped_CFD-LM-246-087-N_2048FC_F.png',1)
cv2.imshow('image', img)
# resizedImage = cv2.resize(img, (400, 400))
# croppedImage = img[500:1520, 570:1480]
# cv2.imshow('image', croppedImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('cropped_CFD-LM-246-087-N_2048FC_F.png',croppedImage)
r = 400.0 / img.shape[1]
dim = (400, int(img.shape[0] * r))
# (400, 400)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)
cv2.imwrite('resized_CFD-LM-246-087-N_2048FC_F.png',resized)
