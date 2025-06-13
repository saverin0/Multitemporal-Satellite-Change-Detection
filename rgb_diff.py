import rasterio
import numpy as np
import matplotlib.pyplot as plt

def read_image(path):
    with rasterio.open(path) as src:
        # Read all bands: shape (bands, height, width)
        img = src.read()
        # Transpose to (height, width, bands)
        img = np.transpose(img, (1, 2, 0))
    return img

# Read images
img_2020 = read_image('images/berlin_2020.tif')
img_2024 = read_image('images/berlin_2024.tif')

print("Image 2020 shape:", img_2020.shape)
print("Image 2024 shape:", img_2024.shape)

def compute_rgbnir_diff(img1, img2):
    # Convert to float to avoid overflow during subtraction
    diff = np.abs(img2.astype(float) - img1.astype(float))
    return diff

def show_diff_maps(diff_img, titles=['Red Diff', 'Green Diff', 'Blue Diff', 'NIR Diff']):
    plt.figure(figsize=(16, 4))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(diff_img[:, :, i], cmap='hot')
        plt.title(titles[i])
        plt.colorbar(shrink=0.7)
        plt.axis('off')
    plt.suptitle('RGB + NIR Band Differences (2024 - 2020)')
    plt.show()

# Assuming img_2020 and img_2024 are loaded and same shape
rgbnir_diff = compute_rgbnir_diff(img_2020, img_2024)

# Visualize the differences
show_diff_maps(rgbnir_diff)
