import json
import folium
from pathlib import Path


def createCommunityDistrictsLayer():
  community_districts_layer = folium.FeatureGroup(name='Community Districts')

  with open(f'{Path.cwd()}/rawData/geo-rawData/community-districts.geojson') as rawData:
    community_districts_geo = json.load(rawData)

  folium.GeoJson(
    community_districts_geo,
    style_function=lambda function: {'fillColor': 'gray', 'color': 'black', 'weight': 2, 'fillOpacity': 0.2}
  ).add_to(community_districts_layer)

  return community_districts_layer