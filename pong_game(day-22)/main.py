from turtle import Screen, Turtle
from paddle import Paddle
from net import Net
from ball import Ball
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()

screen.listen()
screen.onkey(l_paddle.left_up, "w")
screen.onkey(l_paddle.left_down, "s")
screen.onkey(r_paddle.left_up, "Up")
screen.onkey(r_paddle.left_down, "Down")

it_is_on = True
while it_is_on:
    screen.update()
    time.sleep(0.1)
    l_score = 0
    r_score = 0
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() < -380:
        r_score += 1
        ball.reset_ball()
        print(r_score)

    if ball.xcor() > 380:
        l_score += 1
        ball.reset_ball()
        print(l_score)




screen.exitonclick()