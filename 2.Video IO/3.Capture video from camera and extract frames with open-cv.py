import cv2
import matplotlib.pyplot as plt

vc = cv2.VideoCapture(0)
is_capturing, frame = vc.read()

frame_indx = 1
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

def read_one_frame(vc):
    if vc.isOpened():
        is_capturing, frame = vc.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        plt.imshow(img)
        plt.axis('off')
        plt.show()
        return img
    else:
        print("Error: Could not open video stream or file")

# ----------------------------------- main part -----------------------------------------
while is_capturing:
    if frame_indx > 10:
        break
    else:
        f = read_one_frame(vc)
        # this line is so important for save your video in your pc
        out.write(f)
        frame_indx += 1

vc.release()


