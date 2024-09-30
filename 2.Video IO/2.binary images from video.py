from skimage.filters import threshold_otsu
import skvideo.io
import numpy as np
import matplotlib.pyplot as plt
import resize_video as rv
import os
import cv2

# make a resized video, if it is not exist
path = '../images-videos/Coffee1.mp4'
if not os.path.isfile(path):
    rv.resized_video('../images-videos/Coffee.mp4', '../images-videos/Coffee1.mp4', 135, 240)

reader = skvideo.io.FFmpegReader('../images-videos/Coffee.mp4')

num_frames, h, w, num_channels = reader.getShape()
print(num_frames, h, w, num_channels)

plt.figure(figsize=(10, 10))

frame_list = np.random.choice(num_frames, 4)

def show_one_binary_frame(num_frame, binary_frame):
    plt.subplot(2, 2, i + 1)
    plt.imshow(binary_frame)
    plt.axis('off')
    plt.title("Frame {}".format(num_frame), size=15)

def get_one_frame(num_frame):
    reader = skvideo.io.FFmpegReader('../images-videos/Coffee.mp4')
    c = 0
    for f in reader:
        if c == num_frame:
            return f
        else:
            c += 1

def convert2binary_one_frame(num_frame):
    frame = get_one_frame(num_frame)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = threshold_otsu(gray_frame)
    binary_img = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)

    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            if frame[i][j][0] > thresh and frame[i][j][1] > thresh and frame[i][j][2] > thresh:
                binary_img[i][j][0] = 255
                binary_img[i][j][1] = 255
                binary_img[i][j][2] = 255
            elif frame[i][j][0] < thresh and frame[i][j][1] < thresh and frame[i][j][2] < thresh:
                binary_img[i][j][0] = 0
                binary_img[i][j][1] = 0
                binary_img[i][j][2] = 0
    return binary_img

for i in range(len(frame_list)):
    binary_image = convert2binary_one_frame(frame_list[i])
    show_one_binary_frame(frame_list[i], binary_image)

plt.tight_layout()
plt.show()
