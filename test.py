import matplotlib.pyplot as plt
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
from PIL import Image

# Load the image
image_path = './lenna-resized.jpg'  # Replace with the path to your image
image = Image.open(image_path)

# Convert image to numpy array
image_array = np.array(image)

# Extract the red channel (assuming the image is RGB)
red_channel = image_array[:, :, 0]

# Create meshgrid for pixel positions
x = np.arange(0, red_channel.shape[1])
y = np.arange(0, red_channel.shape[0])
x, y = np.meshgrid(x, y)

# Create a figure for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface for the red channel
ax.plot_wireframe(x, y, red_channel, color='r', linewidth=0.5)

# Set labels and title
ax.set_title('3D plot for the Red Channel')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Red Intensity')

plt.show()
