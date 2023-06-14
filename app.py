import tkinter as tk
import requests
import json


def search_license_plates():
    car_color = color_entry.get()
    car_model = model_entry.get()
    license_plate_partial = plate_entry.get()

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
                    if license_plate_partial[i] != "X" and license_plate_partial[i] != full_license_plate[i]:
                        is_match = False
                        break
                if is_match:
                    matching_license_plates.append(record["mispar_rechev"])

    result_label.config(text="Optional IDs: " + str(matching_license_plates))


# Create the Tkinter window
window = tk.Tk()
window.title("Car Plate IL Search")
window.geometry("400x250")
window.configure(bg="#f0f0f0")

# Create and position input labels
color_label = tk.Label(window, text="Car Color:", bg="#f0f0f0", fg="#333333", font=("Arial", 12, "bold"))
color_label.place(x=50, y=30)
model_label = tk.Label(window, text="Car Model:", bg="#f0f0f0", fg="#333333", font=("Arial", 12, "bold"))
model_label.place(x=50, y=70)
plate_label = tk.Label(window, text="License Plate Partial:", bg="#f0f0f0", fg="#333333", font=("Arial", 12, "bold"))
plate_label.place(x=20, y=110)

# Create and position input entry fields
color_entry = tk.Entry(window, width=30)
color_entry.place(x=200, y=30)
model_entry = tk.Entry(window, width=30)
model_entry.place(x=200, y=70)
plate_entry = tk.Entry(window, width=30)
plate_entry.place(x=200, y=110)

# Create search button
search_button = tk.Button(window, text="Search", command=search_license_plates, width=20, bg="#555555", fg="#ffffff",
                          font=("Arial", 12, "bold"))
search_button.place(x=150, y=160)

# Create and position result label
result_label = tk.Label(window, font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333")
result_label.place(x=50, y=200)

# Run the Tkinter event loop
window.mainloop()
