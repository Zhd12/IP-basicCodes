from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
import skvideo.io
import numpy as np
import matplotlib.pyplot as plt

reader = skvideo.io.FFmpegReader('../Coffee.mp4')
# writer = skvideo.io.FFmpegWriter('../Coffee.mp4')

# for frame in reader:
#     gray_frame = rgb2gray(frame)
#     thresh = threshold_otsu(gray_frame)
#
#     binary_img = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
#
#     for i in range(frame.shape[0]):
#         for j in range(frame.shape[1]):
#             binary_img[..., 0] = 255 * (frame[i][j][0] > thresh).astype(np.uint8)
#             binary_img[..., 1] = 255 * (frame[i][j][1] > thresh).astype(np.uint8)
#             binary_img[..., 2] = 255 * (frame[i][j][2] > thresh).astype(np.uint8)
#     writer.writeFrame(binary_img)
#     writer.close()

num_frames, h, w, num_channels = reader.getShape()
print(num_frames, h, w, num_channels)

plt.figure(figsize=(10, 10))

frame_list = np.random.choice(num_frames, 4)

def show_one_frame(frame):
    reader = skvideo.io.FFmpegReader('../Coffee.mp4')
    count = 0
    for f in reader:
        if count == frame:
            plt.subplot(2, 2, i+1)
            plt.imshow(f)
            plt.axis('off')
            plt.title("Frame {}".format(count), size=15)
            break
        else:
            count += 1


def get_one_frame(num_frame):
    reader = skvideo.io.FFmpegReader('../Coffee.mp4')
    c = 0
    for f in reader:
        if c == num_frame:
            return f
        else:
            c += 1

def convert2binary_one_frame(num_frame):
    writer = skvideo.io.FFmpegWriter('../Coffee.mp4')
    frame = get_one_frame(num_frame)
    gray_frame = rgb2gray(frame)
    thresh = threshold_otsu(gray_frame)
    binary_img = np.zeros((frame.shape[0], frame.shape[1], 3), dtype=np.uint8)
    for i in range(frame.shape[0]):
        for j in range(frame.shape[1]):
            binary_img[..., 0] = 255 * (frame[i][j][0] > thresh).astype(np.uint8)
            binary_img[..., 1] = 255 * (frame[i][j][1] > thresh).astype(np.uint8)
            binary_img[..., 2] = 255 * (frame[i][j][2] > thresh).astype(np.uint8)
            print(i, j)
    writer.writeFrame(binary_img)
    writer.close()
    return binary_img

for i in range(len(frame_list)):
    binary_image = convert2binary_one_frame(frame_list[i])
    # print(binary_image)
    show_one_frame(binary_image)

plt.tight_layout()
plt.show()


