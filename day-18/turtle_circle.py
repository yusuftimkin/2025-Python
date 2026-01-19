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

for angle in range (10, 361, 10):

    ada.speed(10)

    ada.pencolor(random_colour())
    
    ada.circle(100)

    ada.setheading(angle)









screen = t.Screen()

screen.exitonclick()