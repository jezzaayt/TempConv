import json
import os
import GUII
counter = 1
def save_data(original,temp, units, date, time):
    global counter 

    data = {
        "ID":counter,
        "Original Value": original,
        "Temperature": temp,
        "Units": units, 
        "Date": date, 
        "Time": time
    }
    
    filename = "temperature_data.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
            
    else:
        existing_data = []
    
    existing_data.append(data)
    counter += 1

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)
        print("Temperature data saved successfully.")
  
    
