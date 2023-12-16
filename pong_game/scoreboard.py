from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-90, 200)
        self.write(self.l_score, align='center', font= ("Courier", 60, "normal"))
        self.goto( 90, 200)
        self.write(self.r_score, align='center', font= ("Courier", 60, "normal"))
    
    def l_point(self):
        self.clear()
        self.l_score += 1
        self.write_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.write_score()