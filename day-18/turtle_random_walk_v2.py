import turtle as t
import random

ada = t.Turtle()

ada.shape("turtle")
ada.color("green")

t.colormode(255)

def random_colour():
    r = random.randint(0 , 255)
    g = random.randint(0 , 255)
    b = random.randint(0 , 255)

    col_ran = (r, g, b)

    return col_ran


directions = ["right", "left"]
angle = [0,90,180, 270]

nums_steps = int(input("How many steps? "))

current_step = 0

pen_size = 10

speed = 1

while current_step <= nums_steps:

    ada.pencolor(random_colour())
    ada.pensize(pen_size)

    if speed == 10:
        speed = 10
        
    ada.setheading(random.choice(angle))
    ada.speed(speed)
    ada.forward(50)
    current_step += 1
    pen_size += 0.5
    speed += 0.25










    

screen = t.Screen()

screen.exitonclick()