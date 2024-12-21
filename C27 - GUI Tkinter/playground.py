#Unlimited Positional Arguments
def add(*args):
    sum=0
    for arg in args:
        sum+=arg


print(add(1, 2, 3, 4, 5))  # Output: (1, 2, 3, 4, 5)

def calculate(n, **kwargs):
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)  # Output: 25