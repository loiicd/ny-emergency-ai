import pandas as pd
import joblib


def predict(FEATURES, incident):
  df = pd.DataFrame(incident)

  features = df[FEATURES]

  categories = joblib.load('./models/categories.pkl')

  features_dummies = pd.get_dummies(features).reindex(columns=categories, fill_value=0)

  linear_regression_from_joblib = joblib.load('./models/model.pkl') 

  predictions = linear_regression_from_joblib.predict(features_dummies)

  print(predictions)

predict