import json
import os
import GUII
def save_data(original,temp, units, date, time):

   
    temp = round(float(temp),3)
    original = round(float(original),3)
    data = {
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

    

    with open(filename, "w") as file:
        json.dump(existing_data, file, indent=4)
        print("Temperature data saved successfully.")
  

def check_json():
    filename = "temperature_data.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
            
    else:
        existing_data = []
    return existing_data