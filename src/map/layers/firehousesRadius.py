import folium
import pandas as pd


def createFirehousesRadiusLayer():
  firehouses_radius_layer = folium.FeatureGroup(name='Firehouses Radius', show=False)

  locations = pd.read_csv('/Users/loic.doerr/dev/ny-emergency-ai/data/locations/FDNY_Firehouse_Listing_20240603.csv')

  for index, location in locations.iterrows():
    lat = location['Latitude']
    lng = location['Longitude']
    folium.Circle([lat, lng], radius=1000, fill_color='red', fill_opacity=0.2, color=None).add_to(firehouses_radius_layer)
    folium.Circle([lat, lng], radius=2000, fill_color='red', fill_opacity=0.1, color=None).add_to(firehouses_radius_layer)

  return firehouses_radius_layer