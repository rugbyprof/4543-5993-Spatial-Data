import json
from rich import print

import random


def random_hex_color():
    # Generate a random integer between 0 and 0xFFFFFF (16777215)
    random_int = random.randint(0, 0xFFFFFF)

    # Format it as a 6-digit hex string, padding with leading zeros if necessary
    return f"#{random_int:06x}"




with open("meteorites_export.json", "r") as f:
    meteorites = json.load(f)

# print(data)
reclasses = {}

geojson = {
  "type": "FeatureCollection",
  "features": []
}





for meteorite in meteorites:
    if meteorite["GeoLocation"] != "":
        # if meteorite["nametype"] != "Valid":
        #     print(f"Nametype {meteorite['nametype']} {meteorite['id']}")
        geolocation = meteorite["GeoLocation"].strip("()").split(", ")
        lat = float(geolocation[0])
        lon = float(geolocation[1])

        if lat==0.0 or lon==0.0:
            continue

        recclass= meteorite.get("recclass", "Unknown")
        feature = {
            "type": "Feature",
            "properties": {
                "name": meteorite.get("name", "Unknown"),
                "mass": meteorite.get("mass", "Unknown"),
                "year": meteorite.get("year", "Unknown"),
                "id": meteorite.get("id", "Unknown"),
                "fall": meteorite.get("fall", "Unknown"),
                "recclass": recclass,
                "marker-color":random_hex_color(),
                "marker-size":"small"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [lon, lat]
            }
        }
    
        if recclass not in reclasses:
            reclasses[recclass] = 0
        reclasses[recclass] += 1
        geojson["features"].append(feature)

sorted_by_key = dict(sorted(reclasses.items(), key=lambda item: item[0]))

# print(sorted_by_key)
# print(geojson)

with open("meteorites.geojson", "w") as f:
    json.dump(geojson, f, indent=2)