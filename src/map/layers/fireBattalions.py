import json
import folium
from pathlib import Path


def createFireBattalionsLayer():
  fire_battalions_layer = folium.FeatureGroup(name='Fire Battalions', show=False)

  with open(f'{Path.cwd()}/data/geo-data/fire-battalions.geojson') as rawData:
    fire_battalions = json.load(rawData)

  folium.GeoJson(fire_battalions, style_function=lambda function: {'fillColor': 'gray', 'color': 'black', 'weight': 2, 'fillOpacity': 0.2}).add_to(fire_battalions_layer)

  return fire_battalions_layer