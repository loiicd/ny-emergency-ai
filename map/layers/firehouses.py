import folium
import pandas as pd
from pathlib import Path


def createFirehousesLayer():
  firehouses_layer = folium.FeatureGroup(name='Firehouses', show=False)

  locations = pd.read_csv(f'{Path.cwd()}/rawData/locations/FDNY_Firehouse_Listing_20240603.csv')

  for index, location in locations.iterrows():
    lat = location['Latitude']
    lng = location['Longitude']
    folium.Circle([lat, lng], radius=20, fill_color='purple', fill_opacity=1, color='purple').add_to(firehouses_layer)

  return firehouses_layer