from flask import Flask, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search_license_plates():
    if request.method == 'POST':
        car_color = request.form.get('car_color')
        car_model = request.form.get('car_model')
        license_plate_partial = request.form.get('license_plate_partial')

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
                full_license_plate = str(record['mispar_rechev'])
                if len(license_plate_partial) == len(full_license_plate):
                    is_match = True
                    for i in range(len(license_plate_partial)):
                        if (
                            license_plate_partial[i] != "X"
                            and license_plate_partial[i] != full_license_plate[i]
                        ):
                            is_match = False
                            break
                    if is_match:
                        matching_license_plates.append(record["mispar_rechev"])

        result_html = f"<h1>Optional IDs: {matching_license_plates}</h1>"

        return '''
        <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                }

                form {
                    width: 300px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 5px;
                    box-shadow: 0px 2px 5px 0px rgba(0, 0, 0, 0.3);
                }

                label {
                    display: block;
                    margin-bottom: 10px;
                    font-weight: bold;
                }

                input[type="text"] {
                    width: 100%;
                    padding: 8px;
                    font-size: 14px;
                    border: 1px solid #ccc;
                    border-radius: 3px;
                }

                input[type="submit"] {
                    width: 100%;
                    padding: 8px;
                    font-size: 14px;
                    color: #ffffff;
                    background-color: #555555;
                    border: none;
                    border-radius: 3px;
                    cursor: pointer;
                }

                /* Custom colors */
                label {
                    color: #333333;
                }

                input[type="text"] {
                    background-color: #f5f5f5;
                    border-color: #999999;
                }

                input[type="submit"] {
                    background-color: #55aaff;
                }

                .result {
                    margin-top: 20px;
                    padding: 10px;
                    background-color: #f5f5f5;
                    border: 1px solid #999999;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <form method="post">
                <label for="car_color">Car Color:</label>
                <input type="text" id="car_color" name="car_color"><br><br>
                <label for="car_model">Car Model:</label>
                <input type="text" id="car_model" name="car_model"><br><br>
                <label for="license_plate_partial">License Plate Partial:</label>
                <input type="text" id="license_plate_partial" name="license_plate_partial"><br><br>
                <input type="submit" value="Search">
            </form>

            <div class="result">
               '''+result_html+'''
            </div>
        </body>
        </html>
        '''

    return '''
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
            }

            form {
                width: 300px;
                margin: 0 auto;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 5px;
                box-shadow: 0px 2px 5px 0px rgba(0, 0, 0, 0.3);
            }

            label {
                display: block;
                margin-bottom: 10px;
                font-weight: bold;
            }

            input[type="text"] {
                width: 100%;
                padding: 8px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 3px;
            }

            input[type="submit"] {
                width: 100%;
                padding: 8px;
                font-size: 14px;
                color: #ffffff;
                background-color: #555555;
                border: none;
                border-radius: 3px;
                cursor: pointer;
            }

            /* Custom colors */
            label {
                color: #333333;
            }

            input[type="text"] {
                background-color: #f5f5f5;
                border-color: #999999;
            }

            input[type="submit"] {
                background-color: #55aaff;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <label for="car_color">Car Color:</label>
            <input type="text" id="car_color" name="car_color"><br><br>
            <label for="car_model">Car Model:</label>
            <input type="text" id="car_model" name="car_model"><br><br>
            <label for="license_plate_partial">License Plate Partial:</label>
            <input type="text" id="license_plate_partial" name="license_plate_partial"><br><br>
            <input type="submit" value="Search">
        </form>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run()
