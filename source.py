import ee
ee.Initialize()

# AOI: Berlin, Germany
aoi = ee.Geometry.Rectangle([13.2, 52.3, 13.6, 52.7])

# Function to get a Sentinel-2 image within a date range
def get_sentinel_image(start_date, end_date):
    return (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
              .filterBounds(aoi)
              .filterDate(start_date, end_date)
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE', 10))
              .sort('CLOUDY_PIXEL_PERCENTAGE')
              .first()
              .clip(aoi)
              .select(['B4', 'B3', 'B2', 'B8']))  # Red, Green, Blue, NIR

# Choose time periods
image_2020 = get_sentinel_image('2020-06-01', '2020-06-30')
image_2024 = get_sentinel_image('2024-06-01', '2024-06-30')

# Export to Drive
export_2020 = ee.batch.Export.image.toDrive(
    image=image_2020,
    description='Sentinel2_Berlin_2020',
    folder='EarthEngine',
    fileNamePrefix='berlin_2020',
    region=aoi,
    scale=10,
    maxPixels=1e9
)

export_2024 = ee.batch.Export.image.toDrive(
    image=image_2024,
    description='Sentinel2_Berlin_2024',
    folder='EarthEngine',
    fileNamePrefix='berlin_2024',
    region=aoi,
    scale=10,
    maxPixels=1e9
)

export_2020.start()
export_2024.start()

print("Export started. Monitor at https://code.earthengine.google.com/tasks")
