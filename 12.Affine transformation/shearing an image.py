from skimage.io import imread
from scipy.ndimage import affine_transform
import numpy as np
import matplotlib.pyplot as plt
img = imread('../images-videos/lenna.jpg')
img = np.array(img)

Shear_x = 0.2
Shear_y = 0.3

# define the shear matrix
# shear in x direction
shear_matrix_x = np.array([[1, Shear_x, 0], [0, 1, 0], [0, 0, 1]])

# shear in y direction
shear_matrix_y = np.array([[1, 0, 0], [-Shear_y, 1, 0], [0, 0, 1]])

# shear in x and y direction
shear_matrix_xy = shear_matrix_x @ shear_matrix_y

# apply the shear transformation
sheared_image_x = affine_transform(img, shear_matrix_x)
sheared_image_y = affine_transform(img, shear_matrix_y)
sheared_image_xy = affine_transform(img, shear_matrix_xy)

plt.figure(figsize=(8, 8))

plt.subplot(221)
plt.imshow(img)
plt.title('Original Image', size=21)
plt.axis('off')

plt.subplot(222)
plt.imshow(sheared_image_x)
plt.title('Sheared Image-x', size=21)
plt.axis('off')

plt.subplot(223)
plt.imshow(sheared_image_y)
plt.title('Sheard Image-y', size=21)
plt.axis('off')

plt.subplot(224)
plt.imshow(sheared_image_xy)
plt.title('Sheard Image-xy', size=21)
plt.axis('off')

plt.show()


