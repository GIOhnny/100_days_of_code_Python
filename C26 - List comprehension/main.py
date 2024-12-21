numbers = [1,2,3]
new_list = [n+1 for n in numbers]

print(new_list)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [ int(n) for n in list_of_strings ]
result = [ even for even in numbers if even % 2 == 0]
print(result)