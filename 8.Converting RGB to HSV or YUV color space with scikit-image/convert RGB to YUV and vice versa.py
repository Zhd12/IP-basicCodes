from skimage.io import imread
from skimage.color import rgb2yuv, yuv2rgb
import numpy as np
import matplotlib.pyplot as plt

img = imread('../images-videos/lenna.jpg')
img_yuv = rgb2yuv(img)

plt.figure(figsize=(20, 12))

plt.subplot(231)
plt.imshow(img_yuv[:, :, 0], cmap='gray')
plt.title('h', size=19)
plt.axis('off')

plt.subplot(232)
plt.imshow(img_yuv[:, :, 1], cmap='gray')
plt.title('s', size=19)
plt.axis('off')

plt.subplot(233)
plt.imshow(img_yuv[:, :, 2], cmap='gray')
plt.title('v', size=19)
plt.axis('off')


img_yuv_copy = img_yuv.copy()
img_yuv[:, :, 0] /= 2

plt.subplot(234)
plt.imshow(np.clip(yuv2rgb(img_yuv), 0, 1))
plt.title('original image with Y = Y/2', size=19)
plt.axis('off')

img_yuv = img_yuv_copy
img_yuv[:, :, 1] /= 3
plt.subplot(235)
plt.imshow(np.clip(yuv2rgb(img_yuv), 0, 1))
plt.title('original image with U = U/3', size=19)
plt.axis('off')

img_yuv = img_yuv_copy
img_yuv[:, :, 2] /= 4
plt.subplot(236)
plt.imshow(np.clip(yuv2rgb(img_yuv), 0, 1))
plt.title('original image with V = V/4', size=19)
plt.axis('off')

plt.show()

