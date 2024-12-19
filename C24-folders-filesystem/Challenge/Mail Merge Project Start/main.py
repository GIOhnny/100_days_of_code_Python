#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

import os
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
print(f"script_dir={script_dir}")
file_path = os.path.join(script_dir, "Input\\Letters\\starting_letter.txt")
print(f"file_path={file_path}")
file_path_names = os.path.join(script_dir, "Input\\Names\\invited_names.txt")
print(f"file_path_names={file_path_names}")
file_path_output = os.path.join(script_dir, "Output\\ReadyToSend\\letter_for_")
print(f"file_path_output={file_path_output}")

def write_letter(letter, name):
    with open(file_path_output + name + ".txt", mode="w") as file:
        file.write(letter)

with open(file_path, mode="r") as file:
    letter = file.read()

with open(file_path_names, mode="r") as file:
    while True:
        name = file.readline()
        new_letter = letter.replace("[name]", name.strip())
        write_letter(new_letter, name.strip())
        if not name:
            break