import json
import folium
import pandas as pd
from pathlib import Path


def createBoroughsScoreLayer():
  boroughs_score_layer = folium.FeatureGroup(name='Bororughs Score', show=False)

  df = pd.read_csv(f'{Path.cwd()}/borough_data.csv')

  with open(f'{Path.cwd()}/data/geo-data/boroughs.geojson') as rawData:
    boroughs_boundaries_geo = json.load(rawData)

  borough_population_density = dict(zip(df['Borough'], df['Score']))

  population_density_values = list(borough_population_density.values())

  max_density = max(population_density_values)

  def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)

  folium.GeoJson(
    boroughs_boundaries_geo,
    style_function=lambda feature: {
      'fillColor': 'red',
      'color': 'black',
      'weight': 2,
      'fillOpacity': normalize(
        borough_population_density.get(feature['properties']['boro_name'], 0), 
        0, 
        max_density
      ),
    }
  ).add_to(boroughs_score_layer)

  return boroughs_score_layer