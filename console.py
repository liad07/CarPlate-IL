import requests
import json

car_color = "אדום מטל"#input textbox
car_model = "I10"#input textbox
license_plate_partial = "61XXX55"#input textbox
full_license_plate = "6186755"
url = "https://data.gov.il/api/3/action/datastore_search?resource_id=053cea08-09bc-40ec-8f7a-156f0677aff3&limit=99999999"
filters = {
    'kinuy_mishari': car_model,
    'tzeva_rechev': car_color
}
params = {'filters': json.dumps(filters)}

response = requests.get(url, params=params)


data = response.json()

matching_license_plates = []
if data["result"]["records"]:
    for record in data["result"]["records"]:
        full_license_plate=str(record['mispar_rechev'])
        if len(license_plate_partial) == len(full_license_plate):
            is_match = True
            for i in range(len(license_plate_partial)):
                if license_plate_partial[i] != "X" and license_plate_partial[i] != full_license_plate[i]:
                    is_match = False
                    break
            if is_match:
                matching_license_plates.append(record["mispar_rechev"])
print("optinal id: "+str(matching_license_plates))
