import another_module
print(f"module_var = {another_module.module_var}")

#https://cs111.wellesley.edu/reference/colors
#https://docs.python.org/3/library/turtle.html
from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()