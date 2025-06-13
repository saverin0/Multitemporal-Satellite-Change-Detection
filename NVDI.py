# NDVI = (NIR - RED) / (NIR + RED)
import numpy as np


img_2020="images/berlin_2020.tif"
img_2024="images/berlin_2024.tif"
def compute_ndvi(image):
    nir = image[:, :, 3].astype(float)  # B8
    red = image[:, :, 0].astype(float)  # B4
    ndvi = (nir - red) / (nir + red + 1e-10)
    return ndvi

ndvi_2020 = compute_ndvi(img_2020)
ndvi_2024 = compute_ndvi(img_2024)

# NDVI difference
ndvi_diff = ndvi_2024 - ndvi_2020

# RGB/NIR difference (absolute difference)
rgb_diff = np.abs(img_2024[:, :, :4] - img_2020[:, :, :4])
