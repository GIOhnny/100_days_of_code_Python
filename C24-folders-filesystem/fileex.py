import os
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "myfile.txt")

with open(file_path, mode="a") as file:
    file.write("\nHello World")

with open(file_path, mode="r") as file:
    contents= file.read()    
    print(contents)
