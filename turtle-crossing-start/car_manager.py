from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.car_gen()
        self.car_speed = STARTING_MOVE_DISTANCE

    def car_gen(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_turtle = Turtle(shape= "square")
            new_turtle.color(random.choice(COLORS))
            new_turtle.shapesize(stretch_len=2, stretch_wid=1)
            new_turtle.penup()
            random_y = random.randint(-250, 250)
        
            random_x = random.randint(310, 370)
        
            new_turtle.goto(random_x, random_y)
            self.cars.append(new_turtle)
    
    def move(self):
        for car in self.cars:
            car.backward(self.car_speed)
       
    def speed_up(self):
           self.car_speed += MOVE_INCREMENT
        