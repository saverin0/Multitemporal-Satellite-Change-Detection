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

def compute_ndvi(image):
    red = image[:, :, 0].astype(float)  # Red is band 0
    nir = image[:, :, 3].astype(float)  # NIR is band 3
    ndvi = (nir - red) / (nir + red + 1e-10)
    return ndvi


def show_image(img, title, cmap='RdYlGn'):
    plt.figure(figsize=(6,6))
    plt.imshow(img, cmap=cmap)
    plt.colorbar()
    plt.title(title)
    plt.axis('off')
    plt.show()

# Read images
img_2020 = read_image('images/berlin_2020.tif')
img_2024 = read_image('images/berlin_2024.tif')

print("Image 2020 shape:", img_2020.shape)
print("Image 2024 shape:", img_2024.shape)

# Compute NDVI
ndvi_2020 = compute_ndvi(img_2020)
ndvi_2024 = compute_ndvi(img_2024)

# NDVI difference
ndvi_diff = ndvi_2024 - ndvi_2020

# Visualize
show_image(ndvi_2020, "NDVI 2020")
show_image(ndvi_2024, "NDVI 2024")
show_image(ndvi_diff, "NDVI Difference (2024 - 2020)", cmap='bwr')
for i, band_name in enumerate(['Red', 'Green', 'Blue', 'NIR']):
    print(f"{band_name} band min: {np.min(img_2020[:, :, i])}, max: {np.max(img_2020[:, :, i])}")
