from turtle import Turtle, Screen

ada = Turtle()

ada.shape("turtle")
ada.color("green")

def dash_line(number_of_times, line_length, turtle_name):

    turtle_name.pencolor("blue")

    for times in range(number_of_times):
        turtle_name.forward(line_length)
        turtle_name.pu()
        turtle_name.forward(line_length)
        turtle_name.pd()

dash_line(5, 10, ada)        

screen = Screen()

screen.exitonclick()