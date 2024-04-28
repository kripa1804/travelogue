from PIL import Image
from exif import Image as ExifImage
import piexif
from app.image_metadata import ImageMetadata
import app.utils as utils
import json
import os
from app.opensearch_client import OpenSearchClient

# # Directory path
# directory = '/Users/sri10898/Practise/Travelogue/images'

# # Get all image files in the directory
# image_files = [file for file in os.listdir(directory) if file.endswith(('.jpg', '.jpeg', '.png'))]

# # Process each image
# for image_file in image_files:
#     # Open the image
#     img = Image.open(os.path.join(directory, image_file))
    
#     # Rest of the code for processing the image goes here
#     # ...
#     # ...

# Open the image
img = Image.open('/Users/sri10898/Practise/Travelogue/images/england-london-bridge.jpg')

exif_image = ExifImage('/Users/sri10898/Practise/Travelogue/images/england-london-bridge.jpg')

image_metadata = ImageMetadata.from_exif_image(exif_image)
val_str = image_metadata.to_json()
val = json.loads(val_str)

print(val)

gps_lat_dec = utils.dms_latitude_to_decimal(val)
gps_lon_dec = utils.dms_longitude_to_decimal(val)

val['gps_latitude'] = gps_lat_dec
val['gps_longitude'] = gps_lon_dec

val_updated_str = json.dumps(val)
print(val_updated_str)


os_client = OpenSearchClient('localhost', 9200)
response = os_client.create_document(index='images')
print(response)

response = os_client.client.index(index='images', body=val_updated_str)
print(response)