from turtle import Turtle, Screen

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)
timmy.right(90)
timmy.forward(100)

timmy.penup()
timmy.forward(100)
timmy.pendown()

timmy.color("blue")
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


import heroes
h = heroes.gen()

print(h)

screen = Screen()
screen.exitonclick()