from sklearn.model_selection import cross_val_score, KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import joblib
from sklearn import metrics
import pandas as pd

# ===== Variables =====
ITERATIONS = 20
FEATURES = ['alarm_box_borough', 'zipcode', 'policeprecinct', 'incident_classification']
TARGET_ATTRIBUTE = 'dispatch_response_seconds_qy'
# =====================

def createModel(features, target, iteration):
  # Split the data
  features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.3, random_state=iteration)
  
  # Create a pipeline with feature scaling and linear regression
  pipeline = Pipeline([
      ('scaler', StandardScaler()),
      ('linear_regression', LinearRegression())
  ])
  
  # Fit the model
  pipeline.fit(features_train, target_train)
  
  # Predict
  target_pred = pipeline.predict(features_test)
  
  # Calculate MSE
  mse = metrics.mean_squared_error(target_test, target_pred)
  print(f'Version {iteration} - MSE: {mse}')
  
  # Save the model
  model_filename = f'./models/version-{iteration}-model.pkl'
  joblib.dump(pipeline, model_filename)
  
  # Save categories for later use
  categories = {col: list(features[col].unique()) for col in features.columns}
  joblib.dump(categories, model_filename.replace('-model.pkl', '-categories.pkl'))


df = pd.read_json('/Users/loic.doerr/dev/berlin-emergency-ai/data/fire-incidents/interims.json')
df.dropna(inplace=True)

features = df[FEATURES]
target = df[TARGET_ATTRIBUTE]

features = pd.get_dummies(features)

for iteration in range(ITERATIONS):
  createModel(features, target, iteration)

# Example of cross-validation
kf = KFold(n_splits=5, random_state=42, shuffle=True)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('linear_regression', LinearRegression())
])

scores = cross_val_score(pipeline, features, target, cv=kf, scoring='neg_mean_squared_error')
print(f'Cross-validated MSE: {-scores.mean()}')
