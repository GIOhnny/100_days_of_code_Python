#http://pandas.pydata.org
import pandas, os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "weather_data.csv")

data = pandas.read_csv(file_path)
print(data["temp"])