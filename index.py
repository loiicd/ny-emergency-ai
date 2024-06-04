from src.predict import predict
from src.trainModel import trainModels

# ====== Variables ======
ITERATIONS = 20
TEST_SIZE = 0.3
FEATURES = ['zipcode', 'incident_borough']
TARGET_ATTRIBUTE = 'engines_assigned_quantity'
# =======================


# trainModels(FEATURES, TARGET_ATTRIBUTE, ITERATIONS, TEST_SIZE)


testData =  [{
  "starfire_incident_id": "2100404460110002",
  "incident_datetime": "2021-01-04T00:01:00.000",
  "alarm_box_borough": "MANHATTAN",
  "alarm_box_number": "446",
  "alarm_box_location": "3 AVE & ST. MARKS PL",
  "incident_borough": "MANHATTAN",
  "zipcode": "10006",
  "policeprecinct": "9",
  "citycouncildistrict": "2",
  "communitydistrict": "103",
  "communityschooldistrict": "1",
  "congressionaldistrict": "12",
  "alarm_source_description_tx": "PD Link/Medical",
  "alarm_level_index_description": "Initial Alarm",
  "highest_alarm_level": "First Alarm",
  "incident_classification": "Medical - PD Link 10-91",
  "incident_classification_group": "Medical Emergencies"
}]

predict(FEATURES, testData)