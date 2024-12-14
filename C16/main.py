import another_module
print(f"module_var = {another_module.module_var}")

#https://cs111.wellesley.edu/reference/colors
#https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("aquamarine")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squitle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"

print(table)