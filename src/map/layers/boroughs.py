import json
import folium


def createBoroughsLayer():
  borough_layer = folium.FeatureGroup(name='Boroughs')

  with open('./data/geo-data/boroughs.geojson') as rawData:
    boroughs_boundaries_geo = json.load(rawData)

  folium.GeoJson(
    boroughs_boundaries_geo,
    style_function=lambda feature: {
      'fillColor': 'green' if feature['properties']['boro_name'] == 'Manhattan' else 'blue' if feature['properties']['boro_name'] == 'Brooklyn' else 'red' if feature['properties']['boro_name'] == 'Bronx' else 'orange' if feature['properties']['boro_name'] == 'Queens' else 'purple',
      'color': 'black',
      'weight': 2,
      'fillOpacity': 0.2,
    }
  ).add_to(borough_layer)

  return borough_layer