import pandas as pd

df = pd.read_json('/Users/loic.doerr/dev/ny-emergency-ai/data/fire-incidents/interims.json')

categories = df[['incident_borough', 'zipcode', 'policeprecinct', 'citycouncildistrict', 'communitydistrict', 'communityschooldistrict', 'congressionaldistrict', 'alarm_box_number']]

unique_categories = categories.drop_duplicates()

unique_categories.to_csv('./locations.csv')

# category_list = unique_categories.to_dict(orient='records')

# print(category_list)
