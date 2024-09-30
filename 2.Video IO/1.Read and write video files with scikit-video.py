import numpy as np
import skvideo.io
import matplotlib.pyplot as plt

reader1 = skvideo.io.FFmpegReader('../Coffee.mp4')

num_frames, h, w, num_channels = reader1.getShape()
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

for i in range(len(frame_list)):
    show_one_frame(frame_list[i])

plt.tight_layout()
plt.show()
