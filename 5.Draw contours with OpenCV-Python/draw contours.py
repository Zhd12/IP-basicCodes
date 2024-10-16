import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images-videos/phone.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gry = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret, thresh = cv2.threshold(img_gry, 125, 255, 0)
contours_thresh, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Number of contours found with threshold = " + str(len(contours_thresh)))

plt.figure(figsize=(20, 15))

plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.title('Original image', size=19)
plt.axis('off')

plt.subplot(222)
plt.imshow(img_gry, cmap="gray")
plt.title('Grayscale Image', size=19)
plt.axis('off')

plt.subplot(223)
plt.imshow(thresh, cmap="gray")
plt.title('Threshold image', size=19)
plt.axis('off')

plt.subplot(224)
plt.imshow(cv2.drawContours(np.copy(img), contours_thresh, -1, (0, 255, 0), 2))
plt.title('Contour Lines with Threshold Image', size=19)
plt.axis('off')

plt.show()
