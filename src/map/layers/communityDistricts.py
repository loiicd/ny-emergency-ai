import json
import folium


def createCommunityDistrictsLayer():
  community_districts_layer = folium.FeatureGroup(name='Community Districts')

  with open('/Users/loic.doerr/dev/ny-emergency-ai/data/geo-data/community-districts.geojson') as rawData:
    community_districts_geo = json.load(rawData)

  folium.GeoJson(
    community_districts_geo,
    style_function=lambda function: {'fillColor': 'gray', 'color': 'black', 'weight': 2, 'fillOpacity': 0.2}
  ).add_to(community_districts_layer)

  return community_districts_layer