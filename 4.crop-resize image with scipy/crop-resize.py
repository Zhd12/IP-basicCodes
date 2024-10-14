from scipy import ndimage
import cv2

img = cv2.imread('../images-videos/lenna-resized.jpg')
resized_img = ndimage.zoom(img, (2, 2, 1), mode='nearest', order=1)

print(img.shape, resized_img.shape)

x_start, x_end = 40, 190
y_start, y_end = 10, 170

cropped_img = img[y_start:y_end, x_start:x_end]

cv2.imshow('original', img)
cv2.imshow('resized', resized_img)
cv2.imshow('cropped image', cropped_img)
cv2.waitKey(0)
