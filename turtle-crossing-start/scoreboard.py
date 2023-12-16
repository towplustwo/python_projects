FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-210, 260)
        self.write_score()
        
    def finish(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='center', font= FONT)

    def write_score(self):
        self.write(f"Level: {self.level}", align='center', font= FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font= FONT)
