import cv2
import numpy as np
import matplotlib.pyplot as plt

def count_objects(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gry = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    binary_img = cv2.threshold(img_gry, 215, 255, cv2.THRESH_BINARY_INV)[1]

    kernel = np.ones((5, 5), np.uint8)
    binary_img_1 = cv2.morphologyEx(binary_img, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(binary_img_1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    output = img.copy()
    cv2.drawContours(output, contours, -1, (0, 255, 0), thickness=2)

    text = "Found {} objects".format(len(contours))
    cv2.putText(output, text, (105, 145), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    print(text)
    return binary_img, output

img = cv2.imread('../images-videos/GreekAlphabet.jpg')
bin_output, output = count_objects(img)

plt.figure(figsize=(20, 7))

plt.subplot(131)
plt.imshow(img)
plt.axis('off')
plt.title('Original Image', size=19)

plt.subplot(132)
plt.imshow(bin_output, cmap='gray')
plt.axis('off')
plt.title('Binary Image', size=19)

plt.subplot(133)
plt.imshow(output)
plt.axis('off')
plt.title('Counting Objects', size=19)

plt.show()