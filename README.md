# Emergency AI

## Problemstellung

- Vorhersage von "Einsatzverläufen"
- Verbesserung der vorhandenen Infrastruktur

## Datenquelle und Auswahl

| Typ          | Organisation          | Precision | Size              | Vorteile                     | Nachteile                     | 
| ------------ | --------------------- | --------- | ----------------- | ---------------------------- | ----------------------------- | 
| Web Crawling | Feuerwehr Emmendingen | Einsatz   | ca. 4800     rows | ✅ Genaue Daten              | ❌ Aufwand durch Web Crawling | 
| Data Set     | Feuerwehr Berlin      | Tag       | ca. 2300     rows | ✅ Unterschiedliche Datasets | ❌ Tagesdurchschnitt          |
| Data Set     | Feuerwehr NewYork     | Einsatz   | ca. 10300000 rows | ✅ Genaue Daten              | ❌ Wenig Fach Wissen          |

- [Feuerwehr Emmendingen](https://feuerwehr.emmendingen.de/die-gesamtwehr/einsaetze)
- [Feuerwehr Berlin](https://www.berliner-feuerwehr.de/service/open-data/#:~:text=Weiterf%C3%BChrende%20Informationen-,Offene%20Daten%20der%20Berliner%20Feuerwehr,medizinischen%20Notf%C3%A4llen%20und%20im%20Katastrophenschutz.)
- [Feuerwehr NewYork](https://opendata.cityofnewyork.us/data/)

### Feuerwehr Emmendingen
```json
{
  "id": "190",
  "title": "Person in Not, Türöffnung",
  "type": "Person in Notlage",
  "location": "Emmendingen, Bürkle-Bleiche",
  "lat": "48.10767999376639",
  "lng": "7.859310311439673",
  "start_date": "05.06.2024 19:31",
  "end_date": "05.06.2024 20:07",
  "alerting_device": "Funkmeldeempfänger",
  "incident_lead": "R. Kesselring",
  "personal_strength": "18",
  "vehicles": [
    { 
      "id": "EM 10",
      "name": "Kommandowagen",
      "abbrevation": "KdoW",
    }, { 
      "id": "EM 46",
      "name": "Hilfeleistungslöschfahrzeug 20",
      "abbrevation": "HLF 20",
    }
  ],
  "organizations": ["Feuerwehr Emmendingen", "Rettungsdienst", "Polizei"]
}
```

### Feuerwehr Berlin
```json
{
  "mission_created_date": "2024-01-01",
  "mission_count_all": 2338,
  "mission_count_ems": 1671,
  "mission_count_ems_critical": 1116,
  "mission_count_ems_critical_cpr": 21,
  "mission_count_fire": 564,
  "mission_count_technical_rescue": 68,
  "response_time_ems_critical_mean": 619.754262788365,
  "response_time_ems_critical_median": 589.0,
  "response_time_ems_critical_std": 212.4887495117316,
  "response_time_ems_critical_cpr_mean": 494.3888888888889,
  "response_time_ems_critical_cpr_median": 493.5,
  "response_time_ems_critical_cpr_std": 146.30634214426246,
  "response_time_fire_time_to_first_pump_mean": 578.2311557788945,
  "response_time_fire_time_to_first_pump_median": 545.0,
  "response_time_fire_time_to_first_pump_std": 213.1385042622863,
  "response_time_fire_time_to_first_ladder_mean": 718.5,
  "response_time_fire_time_to_first_ladder_median": 656.0,
  "response_time_fire_time_to_first_ladder_std": 233.1874475916011,
  "response_time_fire_time_to_full_crew_mean": 803.1335000000001,
  "response_time_fire_time_to_full_crew_median": 754.3715,
  "response_time_fire_time_to_full_crew_std": 229.8317858115656,
  "response_time_technical_rescue_mean": 845.0535714285714,
  "response_time_technical_rescue_median": 712.0,
  "response_time_technical_rescue_std": 375.1114462102191
}
```

### Feuerwehr NewYork
```json
{
  "starfire_incident_id": "2100404460110002",
  "incident_datetime": "2021-01-04T00:01:00.000",
  "alarm_box_borough": "MANHATTAN",
  "alarm_box_number": "446",
  "alarm_box_location": "3 AVE & ST. MARKS PL",
  "incident_borough": "MANHATTAN",
  "zipcode": "10003",
  "policeprecinct": "9",
  "citycouncildistrict": "2",
  "communitydistrict": "103",
  "communityschooldistrict": "1",
  "congressionaldistrict": "12",
  "alarm_source_description_tx": "PD Link/Medical",
  "alarm_level_index_description": "Initial Alarm",
  "highest_alarm_level": "First Alarm",
  "incident_classification": "Medical - PD Link 10-91",
  "incident_classification_group": "Medical Emergencies",
  "dispatch_response_seconds_qy": "13",
  "first_assignment_datetime": "2021-01-04T00:01:00.000",
  "first_activation_datetime": "2021-01-04T00:02:00.000",
  "incident_close_datetime": "2021-01-04T00:07:00.000",
  "valid_dispatch_rspns_time_indc": "N",
  "valid_incident_rspns_time_indc": "N",
  "incident_response_seconds_qy": "0",
  "incident_travel_tm_seconds_qy": "0",
  "engines_assigned_quantity": "1",
  "ladders_assigned_quantity": "0",
  "other_units_assigned_quantity": "0"
}
```

> Gewonnen hat das Dataset von NewYork durch der sehr großen Datenmengen und Möglichkeiten es mit anderen DataSets zu verknüpfen

## Kontext: New York

![NewYork Map][./assets/newYorkMapWithFireBattaltions.png]

## Vorbereitung

### Datenbereinigung
### Packages
### Korrelationsanalyse

## Modelltraining und -bewertung

Für das Modelltraining habe ich Scikit und Linear Regression genutzt

``` py

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

models = []
errors = []

for iteration in range(ITERATIONS):
  features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=TEST_SIZE, random_state=iteration) 
  model = LinearRegression()
  model.fit(features_train, target_train)
  target_pred = model.predict(features_test)
  mse = metrics.mean_squared_error(target_test, target_pred)
  models.append(model)
  errors.append(mse)

print('Errors', errors)

```

## Ergebnisse

## Lessons Learned