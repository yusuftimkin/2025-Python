from turtle import Turtle, Screen
import random

ada = Turtle()

ada.shape("turtle")
ada.color("green")

colours = ["blue", "red", "yellow", "green", "black"]

number_of_sides = int(input("Please enter the number of sides: "))
max_number_of_sides = int(input("Please enter the max number of sides: "))

def turtle_draw_shapes(number_of_sides, turtle_name):

    angle = 360 / number_of_sides

    for lines in range(number_of_sides):
    
        turtle_name.right(angle)
        turtle_name.forward(100)

ada.pencolor(random.choice(colours))
    

while number_of_sides <= max_number_of_sides:

    turtle_draw_shapes(number_of_sides, ada)

    number_of_sides += 1

    ada.pencolor(random.choice(colours))
    
    

screen = Screen()

screen.exitonclick()