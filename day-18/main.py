from turtle import Turtle, Screen
import random

ada = Turtle()

ada.shape("turtle")
ada.color("green")

colours = ["blue", "red", "yellow", "green", "black"]
directions = ["right", "left"]
angle = [0,90,180, 270]

nums_steps = int(input("How many steps? "))

current_step = 0

pen_size = 10

speed = 1

while current_step <= nums_steps:

    ada.pencolor(random.choice(colours))
    ada.pensize(pen_size)

    if speed == 10:
        speed = 10
        
    ada.setheading(random.choice(angle))
    ada.speed(speed)
    ada.forward(50)
    current_step += 1
    pen_size += 0.5
    speed += 0.25










    

screen = Screen()

screen.exitonclick()