import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter, map_coordinates

# 1.Load the original image
img = cv2.imread('../images-videos/lenna.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def generate_displacement(sigma, alpha):
    # 2.Generate random displacement fields(dx, dy)
    shape = img.shape
    dx = np.random.uniform(-1, 1, shape)
    dy = np.random.uniform(-1, 1, shape)

    # 3.Smooth the displacements with gaussian filter
    dx = gaussian_filter(dx, sigma=sigma, mode='constant', cval=0) * alpha
    dy = gaussian_filter(dy, sigma=sigma, mode='constant', cval=0) * alpha
    return dx, dy


def elastic_deformation(image, dx, dy):
    # 4.Generate new coordinate grid
    x, y = np.meshgrid(np.arange(image.shape[1]), np.arange(image.shape[0]))
    x_new = x + dx
    y_new = y + dy

    # 5. Apply the deformation to each channel separatedly
    deformed_img = map_coordinates(img, [y_new, x_new], mode='reflect', order=1)

    return deformed_img

shape = img.shape
sigma = 4
alpha = 50
dx, dy = generate_displacement(sigma, alpha)
deformed_img = elastic_deformation(img, dx, dy)

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Original image', size=14)
plt.axis('off')

plt.subplot(122)
plt.imshow(deformed_img, cmap='gray')
plt.title('deformed image', size=14)
plt.axis('off')

plt.show()