from turtle import Turtle, Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width= 800, height =600)
screen.title("Pong Game")
screen.tracer(0)


line = Turtle()
line.color("white")
line.hideturtle()
line.speed("fastest")
line.penup()
line.goto(0, 280)
line.width(6)


for _ in range(0, 14):
    line.setheading(270)
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)
    
# paddle 
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up ,"Up")
screen.onkey(r_paddle.go_down ,"Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "f")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect collision with opp walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        

    if ball.xcor() > 380 :
        ball.reset()
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() < -380 :
        ball.reset()
        scoreboard.r_point()




































screen.exitonclick()