import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../images-videos/lenna.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def gamma_correction(img, gamma):
    # Create an empty lookup table with 256 elements, each element is an unsigned 8-bit integer
    lookup_table = np.empty((1, 256), np.uint8)

    # Loop through each possible pixel value (0-255)
    for pixel in range(256):
        # Normalize the pixel value to the range [0, 1]
        normalized_p = pixel / 255
        # Apply gamma correction and scale back to [0, 255], storing it in the lookup table
        lookup_table[0, pixel] = pow(normalized_p, gamma) * 255

    # Apply the lookup table to the image using OpenCV's LUT function and return the result
    return cv2.LUT(img, lookup_table)

plt.figure(figsize=(15, 15))
i = 1
for gm in np.linspace(0, 2, 16):
    new_img = gamma_correction(img, gm)
    plt.subplot(4, 4, i)
    plt.imshow(new_img)
    plt.title(r'$\gamma$={:.2f}'.format(gm), size=17)
    plt.axis('off')
    i += 1
plt.suptitle('Gamma Correction', size=30)
plt.show()
