import numpy as np
from scipy.ndimage import rotate
from skimage.io import imread
import matplotlib.pyplot as plt

img = imread('../images-videos/lenna.jpg')
rotated_img = np.array(rotate(img, angle=45))
plt.figure(figsize=(10, 10))
plt.imshow(rotated_img)
plt.axis('off')
plt.show()