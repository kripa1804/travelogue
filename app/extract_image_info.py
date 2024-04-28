from PIL import Image
from exif import Image as ExifImage
import piexif
from image_metadata import ImageMetadata
import utils as utils
import json
import os
from opensearch_client import OpenSearchClient

# Directory path
directory = os.getcwd() + '/images/'

# Get all image files in the directory
image_files = [file for file in os.listdir(directory) if file.endswith(('.jpg', '.jpeg', '.png'))]
os_client = OpenSearchClient('localhost', 9200)

# Process each image
for image_file in image_files:
#     # Open the image
#     img = Image.open(os.path.join(directory, image_file))

    # Open the image
    image_path = os.path.join(directory, image_file)
    exif_image = ExifImage(image_path)

    image_metadata = ImageMetadata.from_exif_image(exif_image, image_path)
    val_str = image_metadata.to_json()
    val = json.loads(val_str)

    print(val)

    gps_lat_dec = utils.dms_latitude_to_decimal(val)
    gps_lon_dec = utils.dms_longitude_to_decimal(val)

    val['gps_latitude'] = gps_lat_dec
    val['gps_longitude'] = gps_lon_dec
    val['image_path'] = image_path

    val_updated_str = json.dumps(val)
    print(val_updated_str)

    response = os_client.index_document(index='images', body=val_updated_str)
    print(response)