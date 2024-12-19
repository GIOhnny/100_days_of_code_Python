import os, csv
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "weather_data.csv")

with open(file_path) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1])) 
    print(temperatures)