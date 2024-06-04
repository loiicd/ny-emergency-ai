import pandas as pd

df = pd.read_json('/Users/loic.doerr/dev/berlin-emergency-ai/data/fire-incidents/interims.json')

value_counts = df["alarm_level_index_description"].value_counts()
print(value_counts)