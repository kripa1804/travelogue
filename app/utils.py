# Convert DMS latitude to decimal
def dms_latitude_to_decimal(val):
    dms_latitude = val['gps_latitude']
    dms_latitude_ref = val['gps_latitude_ref']
    decimal_latitude = dms_to_decimal(dms_latitude, dms_latitude_ref)
    return decimal_latitude

# Convert DMS longitude to decimal
def dms_longitude_to_decimal(val):
    dms_longitude = val["gps_longitude"]
    dms_longitude_ref = val["gps_longitude_ref"]
    decimal_longitude = dms_to_decimal(dms_longitude, dms_longitude_ref)
    return decimal_longitude

def dms_to_decimal(dms, ref):
    degrees = dms[0]
    minutes = dms[1]
    seconds = dms[2]
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal