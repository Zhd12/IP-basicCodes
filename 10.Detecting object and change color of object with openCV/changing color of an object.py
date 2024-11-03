import cv2
import matplotlib.pyplot as plt
from detecting_object import DetectingObject

img = cv2.imread('../images-videos/horse.jpeg')

l_bnd = (0, 25, 25)
h_bnd = (20, 255, 255)
obj_detect = DetectingObject(img, l_bnd, h_bnd)

changedColor_img = obj_detect.img_rgb.copy()
obj_detect.hsv[:, :, 0:2] = obj_detect.hsv[:, :, 0:2] / 3
changedColor_img[obj_detect.mask1] = cv2.cvtColor(obj_detect.hsv, cv2.COLOR_HSV2RGB)[obj_detect.mask1]
plt.figure(figsize=(20, 10))

plt.subplot(121)
plt.imshow(obj_detect.img_rgb)
plt.axis('off')

plt.subplot(122)
plt.imshow(changedColor_img)
plt.axis('off')
plt.show()

