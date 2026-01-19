from turtle import Turtle, Screen

ada = Turtle()
ada.shape("turtle")
ada.color("green")

ada.forward(100)

ada_destination = ada.pos()

print(ada_destination[0])

yaya = ada.color()

print(yaya[0])






screen = Screen()

screen.exitonclick()