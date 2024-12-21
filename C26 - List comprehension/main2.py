import os
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
file1 = os.path.join(script_dir, "file1.txt")
file2 = os.path.join(script_dir, "file2.txt")

l1 = []
with open(file1, mode="r") as file:
    for v in file:      
        l1.append(int(v.strip()))

l2 = []
with open(file2, mode="r") as file:
    for v in file:      
        l2.append(int(v.strip()))

result = [num for num in l1 if num in l2]

print (result)