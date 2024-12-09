import matplotlib.pyplot as plt

def show_images(images: list, img_title: list, w_fig, h_fig, nrows=1, ncols=1):
    all_num = nrows * ncols
    if all_num > 1:
        fig, axes = plt.subplots(nrows, ncols, figsize=(w_fig, h_fig))
        for i, ax in enumerate(axes):
            ax.imshow(images[i], cmap='gray')
            ax.set_title(img_title[i], size=20)
            ax.axis('off')
    if all_num == 1:
        plt.imshow(images[0], cmap='gray')
        plt.title(img_title[0], size=20)
        plt.axis('off')
    plt.show()