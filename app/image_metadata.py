import json
from dataclasses import dataclass, asdict, field
from typing import List

@dataclass
class ImageMetadata:
    datetime_original: str = field(default=None)
    gps_latitude: List[float] = field(default_factory=list)
    gps_latitude_ref: str = field(default=None)
    gps_longitude: List[float] = field(default_factory=list)
    gps_longitude_ref: str = field(default=None)
    gps_altitude: float = field(default=None)

    def to_json(self):
        return json.dumps(asdict(self), default=str)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))
    
    @classmethod
    def from_exif_image(cls, exif_image):
        return cls(
            datetime_original=exif_image.get("datetime_original"),
            gps_latitude=exif_image.get("gps_latitude"),
            gps_latitude_ref=exif_image.get("gps_latitude_ref"),
            gps_longitude=exif_image.get("gps_longitude"),
            gps_longitude_ref=exif_image.get("gps_longitude_ref"),
            gps_altitude=exif_image.get("gps_altitude"),
        )