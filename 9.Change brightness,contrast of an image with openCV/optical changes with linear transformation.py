import cv2
import matplotlib.pyplot as plt

# Settings for contrast and brightness
alpha = [0.25, 0.5, 1, 1.5, 2.5]  # Contrast factor
beta = [0, 30, 60, 90, 120]  # Brightness factor

def basic_linear_transformation(img, al, bt):
    return cv2.convertScaleAbs(img, alpha=al, beta=bt)

img = cv2.imread('../images-videos/lenna.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20, 20))
i = 1
for al in alpha:
    for bt in beta:
        new_img = basic_linear_transformation(img, al, bt)
        plt.subplot(5, 5, i)
        plt.imshow(new_img)
        plt.title(r'$\alpha$={:.2f}, $\beta$={:.2f}'.format(al, bt), size=17)
        plt.axis('off')
        i += 1
plt.suptitle('Basic linear transform to change brightness', size=30)
plt.show()