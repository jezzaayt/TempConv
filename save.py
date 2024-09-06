import json
import os
import GUII
counter = 1
def save_data(original,temp, units, date, time):
    global counter 
    check_counter(counter)

    c = check_counter(counter)
    print(check_counter(counter))
    data = {
        "ID":c,
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
  

def check_counter(counter):
    # check if counter is in json 
    filename = "temperature_data.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:
                existing_data = json.load(file)
            except json.JSONDecodeError:
                existing_data = []
            
    else:
        existing_data = []
    existing_ids = [item["ID"] for item in existing_data]
    if counter in existing_ids:

        print(existing_ids[-1])
        print(max(existing_ids))
        newCounter = int(counter)
        newCounter = max(existing_ids) + 1
        return newCounter
    return False