import ee
ee.Initialize()

# Example Area of Interest (AOI)
aoi = ee.Geometry.Rectangle([77.5, 28.4, 77.7, 28.6])  # Delhi region

# Load a Sentinel-2 image
image = ee.ImageCollection("COPERNICUS/S2_SR") \
    .filterBounds(aoi) \
    .filterDate("2020-01-01", "2020-01-31") \
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 10)) \
    .first() \
    .clip(aoi) \
    .select(['B4', 'B3', 'B2', 'B8'])  # Red, Green, Blue, NIR

# Start an export task
task = ee.batch.Export.image.toDrive(
    image=image,
    description='Sentinel2_Jan2020',
    folder='EarthEngine',
    fileNamePrefix='sentinel2_jan2020',
    region=aoi,
    scale=10,
    maxPixels=1e9
)

task.start()

print("Export task started. Monitor it at https://code.earthengine.google.com/tasks")
