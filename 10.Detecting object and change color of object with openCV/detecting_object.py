import cv2
import numpy as np
import matplotlib.pyplot as plt

class DetectingObject:
    def __init__(self, img_bgr, low_bound_hsv, high_bound_hsv):
        self.img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        self.hsv = cv2.cvtColor(self.img_rgb, cv2.COLOR_RGB2HSV)
        self.mask = cv2.inRange(self.hsv, low_bound_hsv, high_bound_hsv)
        self.mask1 = self.mask > 0

    def detect(self):
        detected_obj = np.zeros_like(self.img_rgb)
        detected_obj[self.mask1] = self.img_rgb[self.mask1]
        return detected_obj

if __name__ == "__main__":
    img = cv2.imread('../images-videos/horse-r.jpeg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    low_bnd = (0, 25, 25)
    high_bnd = (20, 255, 255)
    obj1 = DetectingObject(img, low_bnd, high_bnd)
    new_img = obj1.detect()

    plt.figure(figsize=(20, 10))

    plt.subplot(121)
    plt.imshow(img_rgb)
    plt.axis('off')

    plt.subplot(122)
    plt.imshow(new_img)
    plt.axis('off')
    plt.show()
