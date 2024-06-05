import random
import datetime

boroughs = ['BRONX', 'MANHATTAN', 'QUEENS', 'RICHMOND / STATEN ISLAND']
alarm_source_description_txs = ['Phone', 'PD Link/Medical', 'EMS Link/Medical']
alarm_level_index_descriptions = ['Initial Alarm', 'Second Alarm', 'Third Alarm']
incident_classification_types = [{'incident_classification': 'Medical - PD Link 10-91', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Medical - Breathing / Ill or Sick', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Medical - EMS Link 10-91', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Medical - Serious Life Threatening', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Medical - No PT Contact EMS is Onscene', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Utility Emergency - Gas', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Automobile Fire', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': "Multiple Dwelling 'A' - Compactor fire", 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Elevator Emergency - Unoccupied', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Medical MFA - EMS Link', 'incident_classification_group': 'Medical MFAs'}, {'incident_classification': 'Non-Medical MFA - ERS No Contact', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Assist Civilian - Non-Medical', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Odor - Other Than Smoke', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': "Multiple Dwelling 'A' - Food on the stove fire", 'incident_classification_group': 'Structural Fires'}, {'incident_classification': "Multiple Dwelling 'A' - Other fire", 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Medical MFA - PD Link', 'incident_classification_group': 'Medical MFAs'}, {'incident_classification': 'Carbon Monoxide - Code 3 - Emergency (over 9 ppm)', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Alarm System - Testing', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Vehicle Accident - Other', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Carbon Monoxide - Code 1 - Investigation', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Medical - Victim Deceased', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Utility Emergency - Water', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Utility Emergency - Steam', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Non-Medical MFA - ERS', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Non-Medical MFA - Phone', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Non-Medical MFA - Private Fire Alarm', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Elevator Emergency - Occupied', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Sprinkler System - Malfunction', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Alarm System - Unnecessary', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Utility Emergency - Electric', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Private Dwelling Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Manhole Fire - Seeping Smoke', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Undefined Emergency', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Alarm System - Defective', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': "Multiple Dwelling 'B' Fire", 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Demolition Debris or Rubbish Fire', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Manhole Fire - Other', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Transit System - NonStructural', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Hospital Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Carbon Monoxide - Code 2 - Incident (1-9 ppm)', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Sprinkler System - Working on System', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Non-Medical MFA - Verbal', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Other Commercial Building Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Odor - Other Smoke', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Other Public Building Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Maritime Emergency', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Defective Oil Burner', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Remove Civilian - Non-Fire', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Utility Emergency - Undefined', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Downed Tree', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Carbon Monoxide - Code 4 - No Detector Activation', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Non-Medical 10-91 (Unnecessary Alarm)', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Brush Fire', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Medical - Assist Civilian', 'incident_classification_group': 'Medical Emergencies'}, {'incident_classification': 'Vehicle Accident - With Extrication', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Non-Medical MFA - BARS', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Other Transportation Fire', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Church Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Non-Medical MFA - ERS Timeout', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Store Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Factory Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Abandoned Derelict Vehicle Fire', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Construction or Demolition Building Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Transit System Emergency', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Carbon Monoxide - No Code', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'School Fire', 'incident_classification_group': 'Structural Fires'}, {'incident_classification': 'Elevator Emergency - Undefined', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Sprinkler System - Other', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Sprinkler System - Activated', 'incident_classification_group': 'NonMedical Emergencies'}, {'incident_classification': 'Non-Medical MFA - ERS No Console Available', 'incident_classification_group': 'NonMedical MFAs'}, {'incident_classification': 'Undefined Nonstructural Fire', 'incident_classification_group': 'NonStructural Fires'}, {'incident_classification': 'Transit System - Structural', 'incident_classification_group': 'Structural Fires'}]

def createFictionalData(quantity: int, attributes: list[str]):
  data = []

  for i in range(quantity):
    incident_classification_type = random.choice(incident_classification_types)
    borough = random.choice(boroughs)
    attribute_values = {
      "starfire_incident_id": random.randint(10000000, 90000000),
      "incident_datetime": datetime.datetime.today().isoformat(),
      "alarm_box_borough": borough,
      "alarm_box_number": random.randint(100, 500),
      "alarm_box_location": "NOSTRAND AVE & LINDEN BLVD",
      "incident_borough": borough,
      "zipcode": random.randint(10000, 50000),
      "policeprecinct": random.randint(10, 100),
      "citycouncildistrict": random.randint(10, 100),
      "communitydistrict": random.randint(10, 100),
      "communityschooldistrict": random.randint(10, 100),
      "congressionaldistrict": random.randint(10, 100),
      "alarm_source_description_tx": random.choice(alarm_source_description_txs),
      "alarm_level_index_description": random.choice(alarm_level_index_descriptions),
      "incident_classification": incident_classification_type['incident_classification'],
      "incident_classification_group": incident_classification_type['incident_classification_group'],
    }

    incident = {attr: attribute_values[attr] for attr in attributes}
    # print(incident)
    data.append(incident)

  # print('Data', data)

  return data


# createFictionalData(3, ['alarm_box_borough', 'incident_classification', 'zipcode'])