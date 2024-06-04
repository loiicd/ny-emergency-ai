from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import joblib
from sklearn import metrics
import pandas as pd


def createModelFile(linear_regression, iteration: int):
  joblib.dump(linear_regression, f'./models/version-{iteration}-model.pkl')


def createCategoryFile(features, iteration: int):
  categories = {col: list(features[col].unique()) for col in features.columns}
  joblib.dump(categories, f'./models/version-{iteration}-categories.pkl')


def calculateMSE(linear_regression, features_test, target_test, iteration):
  target_pred = linear_regression.predict(features_test)

  mse = metrics.mean_squared_error(target_test, target_pred)
  print(f'Version {iteration} - MSE: {mse}')


def createModel(features, target, iteration, TEST_SIZE):
  features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=TEST_SIZE, random_state=iteration) 

  linear_regression = LinearRegression() 

  linear_regression.fit(features_train, target_train)

  calculateMSE(linear_regression, features_test, target_test, iteration)

  createModelFile(linear_regression, iteration)
  createCategoryFile(features, iteration)

def trainModels(FEATURES, TARGET_ATTRIBUTE, ITERATIONS, TEST_SIZE):
  df = pd.read_json('/Users/loic.doerr/dev/berlin-emergency-ai/data/fire-incidents/interims.json')
  df.dropna(inplace=True)

  features = df[FEATURES]
  target = df[TARGET_ATTRIBUTE]

  features = pd.get_dummies(features)

  for iteration in range(ITERATIONS):
    createModel(features, target, iteration, TEST_SIZE)
