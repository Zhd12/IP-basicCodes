from skimage.io import imread
from skimage.util import random_noise, montage
import numpy as np
import matplotlib.pyplot as plt

img = imread('../images-videos/lenna.jpg')
sigma = np.linspace(0, 1, 9)
noisy_images = []

for i in range(len(sigma)):
    noisy_images.append(random_noise(img, var=sigma[i]**2))

c = 1
for i in range(len(sigma)):
    noisy_img = random_noise(img, var=sigma[i]**2)
    plt.subplot(3, 3, c)
    plt.axis('off')
    # plt.title('noisy images before montage')
    plt.imshow(noisy_img)
    c += 1
plt.suptitle('noisy image before montage', fontsize=16)
plt.show()

noisy_images = np.array(noisy_images)

# you should add [channel_axis = -1] in montage function to use it
noisy_images_montage = montage(noisy_images, grid_shape=(3, 3), rescale_intensity=True, channel_axis=-1)

plt.figure(figsize=(15, 15))
plt.imshow(noisy_images_montage)
plt.axis('off')
plt.suptitle('noisy image after montage', fontsize=40)
plt.show()
