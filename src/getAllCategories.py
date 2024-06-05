import pandas as pd

df = pd.read_json('/Users/loic.doerr/dev/ny-emergency-ai/data/fire-incidents/interims.json')

categories = df[['incident_classification', 'incident_classification_group']]

unique_categories = categories.drop_duplicates()

category_list = unique_categories.to_dict(orient='records')

print(category_list)