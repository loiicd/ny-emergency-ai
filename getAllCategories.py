import pandas as pd

df = pd.read_json('/Users/loic.doerr/dev/ny-emergency-ai/data/fire-incidents/interims.json')

categories = df['incident_classification_group'].unique()

print(categories)