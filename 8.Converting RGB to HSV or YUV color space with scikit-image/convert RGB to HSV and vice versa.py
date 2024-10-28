import cv2
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb
import numpy as np
import matplotlib.pyplot as plt

img = imread('../images-videos/lenna.jpg')
img_hsv = rgb2hsv(img)

plt.figure(figsize=(20, 12))

plt.subplot(231)
plt.imshow(img_hsv[:, :, 0], cmap='gray')
plt.title('h', size=19)
plt.axis('off')

plt.subplot(232)
plt.imshow(img_hsv[:, :, 1], cmap='gray')
plt.title('s', size=19)
plt.axis('off')

plt.subplot(233)
plt.imshow(img_hsv[:, :, 2], cmap='gray')
plt.title('v', size=19)
plt.axis('off')


img_hsv_copy = img_hsv.copy()
img_hsv[:, :, 0] /= 4

plt.subplot(234)
plt.imshow(hsv2rgb(img_hsv))
plt.title('original image with h = h/4', size=19)
plt.axis('off')

img_hsv = img_hsv_copy
img_hsv[:, :, 1] /= 3
plt.subplot(235)
plt.imshow(hsv2rgb(img_hsv))
plt.title('original image with s = s/3', size=19)
plt.axis('off')

img_hsv = img_hsv_copy
img_hsv[:, :, 1] /= 5
plt.subplot(236)
plt.imshow(hsv2rgb(img_hsv))
plt.title('original image with v = s/5', size=19)
plt.axis('off')

plt.show()

