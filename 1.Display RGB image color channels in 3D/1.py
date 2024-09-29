import skimage
from skimage.io import imread
import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
# from mpl_toolkits.mplot3d import Axes3D  # Import for 3D plotting


def plot_3d(X, Y, Z, cmap='reds', title='3D Image'):

    """
        This function plots 3D visualization of a channel
        It displays (x, y, f(x,y)) for all x,y values
    """

    fig = plt.figure(figsize=(15, 15))

    # First explicitly create the 3D axes using add_subplot
    fig.add_subplot(111, projection='3d')

    # Automatically rescale Z-values between 34.50 and 265.50
    Z_min, Z_max = Z.min(), Z.max()  # Get original Z min and max
    np.interp(Z, (Z_min, Z_max), (34.50, 265.50))  # Rescale Z to new range (34.50, 265.50)

    ax = fig.gca()
    ax.plot_surface(X, Y, Z, cmap=cmap, linewidth=0, antialiased=False, rstride=2, cstride=2, alpha=.5)

    # Set the tick locations manually with a step of 50
    ax.set_xticks(np.arange(0, X.max() + 1, 50))  # Set x-axis ticks to 0, 50, 100, ...
    ax.set_yticks(np.arange(0, Y.max() + 1, 50))  # Set y-axis ticks similarly
    # ax.set_zticks(np.arange(0, Z.max() + 1, 50))  # Set z-axis ticks similarly

    ax.xaxis.set_major_locator(LinearLocator(10))
    ax.xaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    ax.view_init(elev=10, azim=5)
    ax.set_title(title, size=20)
    plt.show()

# skimage.io.imread('../lenna-resized.jpg', as_gray=False, plugin=None, flatten=None)

# img = cv2.imread('../lenna-resized.jpg')
img = imread('../lenna-resized.jpg')

Y = np.arange(img.shape[0])
X = np.arange(img.shape[1])
X, Y = np.meshgrid(X, Y)

r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

plot_3d(r, X, img.shape[1]-Y, cmap='Reds', title='3D plot for the Red Channel')
plot_3d(g, X, img.shape[1]-Y, cmap='Greens', title='3D plot for the Green Channel')
plot_3d(b, X, img.shape[1]-Y, cmap='Blues', title='3D plot for the Blue Channel')

# cv2.imshow('Original Image', img)
# cv2.waitKey(0)