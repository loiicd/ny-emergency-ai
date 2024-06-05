import random
import datetime

boroughs = ['BRONX', 'MANHATTAN', 'QUEENS', 'RICHMOND / STATEN ISLAND']
alarm_source_description_txs = ['Phone', 'PD Link/Medical', 'EMS Link/Medical']
alarm_level_index_descriptions = ['Initial Alarm', 'Second Alarm', 'Third Alarm']
incident_classifications = ['Medical - Breathing / Ill or Sick', 'Automobile Fire', 'Odor - Other Than Smoke', 'Elevator Emergency - Unoccupied']
incident_classification_groups = ['Medical Emergencies', 'NonMedical Emergencies', 'NonStructural Fires', 'Structural Fires', 'Medical MFAs', 'NonMedical MFAs']

def createFictionalData(quantity: int, attributes: list[str]):
  data = []

  for i in range(quantity):
    attribute_values = {
      "starfire_incident_id": random.randint(10000000, 90000000),
      "incident_datetime": datetime.datetime.today(),
      "alarm_box_borough": random.choice(boroughs),
      "alarm_box_number": random.randint(100, 500),
      "alarm_box_location": "NOSTRAND AVE & LINDEN BLVD",
      "incident_borough": random.choice(boroughs),
      "zipcode": random.randint(10000, 50000),
      "policeprecinct": random.randint(10, 100),
      "citycouncildistrict": random.randint(10, 100),
      "communitydistrict": random.randint(10, 100),
      "communityschooldistrict": random.randint(10, 100),
      "congressionaldistrict": random.randint(10, 100),
      "alarm_source_description_tx": random.choice(alarm_source_description_txs),
      "alarm_level_index_description": random.choice(alarm_level_index_descriptions),
      "incident_classification": random.choice(incident_classifications),
      "incident_classification_group": random.choice(incident_classification_groups),
    }

    for _ in range(quantity):
      incident = {attr: attribute_values[attr] for attr in attributes}
      data.append(incident)

  return data