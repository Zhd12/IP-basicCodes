import numpy as np
import matplotlib.pyplot as plt

im_h = plt.imread(r'D:\Image-Processing-Masterclass\images-videos\lenna.jpg')

# image can be reflected vertically(that is flipped)
flipped_img = np.flipud(im_h)

# image can be reflected horizontally(that is flopped)
flopped_img = np.fliplr(im_h)

plt.figure(figsize=(30, 10))

plt.subplot(131)
plt.imshow(im_h)
plt.axis('off')
plt.title('Original Image', size=21)

plt.subplot(132)
plt.imshow(flipped_img)
plt.axis('off')
plt.title('Flipped Image', size=21)

plt.subplot(133)
plt.imshow(flopped_img)
plt.axis('off')
plt.title('Flopped Image', size=21)

plt.show()
