#http://pandas.pydata.org
import pandas,os

from torch import le

# Activate the virtual environment
# activate_this = os.path.join(os.path.dirname(__file__), '../.venv/Scripts/activate_this.py')
# with open(activate_this) as f:
#     exec(f.read(), {'__file__': activate_this})

# Get the directory of the current script
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "weather_data.csv")

data = pandas.read_csv(file_path)
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(f"Avg temp = {sum(temp_list)/len(temp_list)}")
print(f"Avg temp = {data['temp'].mean()}")

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

monday_temp = monday.temp[0] * 9/5 + 32
print(monday_temp)

#Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

datan = pandas.DataFrame(data_dict)
datan.to_csv(os.path.join(script_dir, "new_data.csv"))

