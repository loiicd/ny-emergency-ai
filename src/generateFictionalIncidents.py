import random
import datetime

BOROUGHS = ['MANHATTAN', 'BROOKLYN', 'QUEENS', 'BRONX', 'RICHMOND / STATEN ISLAND']

HIGHEST_ALARM_LEVELS = ['First Alarm', 'Second Alarm', 'Fourth Alarm', 'Seventh Alarm', 'ALL Hands Working']
HIGHEST_ALARM_LEVELS_WEIGHTS = [10961, 3, 1, 1, 34]

ALARM_SOURCE_DESCRIPTION = ["EMS Link/Medical", "Phone", "PD Link/Medical", "Private Fire Alarm", "Verbal", "ERS No Contact", "911", "ERS", "BARS", "UCT/911", "911 Text", "DEFAULT RECORD"]
ALARM_SOURCE_DESCRIPTION_WEIGHTS = [4216, 3311, 2303, 813, 174, 67, 67, 36, 6, 4, 2, 1]

def generateIncident():
  borough = random.choice(BOROUGHS)

  incident = {
    "starfire_incident_id": "111111111111111",
    "incident_datetime": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
    "alarm_box_borough": borough,
    "alarm_box_number": "2529",
    "alarm_box_location": "M.L.KING JR BLVD & W 165 ST",
    "incident_borough": borough,
    "zipcode": "10452",
    "policeprecinct": "44",
    "citycouncildistrict": "16",
    "communitydistrict": "204",
    "communityschooldistrict": "9",
    "congressionaldistrict": "15",
    "alarm_source_description_tx": random.choices(ALARM_SOURCE_DESCRIPTION, ALARM_SOURCE_DESCRIPTION_WEIGHTS)[0],
    "alarm_level_index_description": "Initial Alarm",
    "highest_alarm_level": random.choices(HIGHEST_ALARM_LEVELS, HIGHEST_ALARM_LEVELS_WEIGHTS)[0],
    "incident_classification": "Medical - EMS Link 10-91",
    "incident_classification_group": "Medical Emergencies",
  }

  print(incident)

generateIncident()

# "2021-01-04T00:10:00.000"