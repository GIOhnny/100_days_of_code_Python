from turtle import Turtle
import os
# Get the directory of the current script
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "data.txt")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier", 20, "normal"))

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game over!", align="center", font=("Courier", 20, "normal"))

    def get_high_score(self):
        with open(file_path, mode="r") as file:
            contents= file.read()
            return int(contents)
        
    def write_high_score(self):
        with open(file_path, mode="w") as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()

        self.score = 0
        self.clear()
        self.update_score()

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_score()