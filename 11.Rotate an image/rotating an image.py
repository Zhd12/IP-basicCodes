from scipy.ndimage import rotate
from skimage.io import imread
import matplotlib.pyplot as plt

img = imread('../images-videos/lenna.jpg')

rotated_img = rotate(img, -30)

plt.figure(figsize=(5, 5))
plt.imshow(rotated_img)
plt.axis('off')
plt.show()
