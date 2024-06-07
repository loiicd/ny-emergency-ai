import pandas as pd


df = pd.read_csv('/Users/loic.doerr/dev/ny-emergency-ai/preparedData/incidents.csv')

df = df.sample(n=50000)

sum = df['engines_assigned_quantity'].sum() / len(df)

print(sum)