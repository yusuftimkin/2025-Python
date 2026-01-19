from turtle import Turtle, Screen
import random


colors = ["red", "yellow", "blue", "orange", "green", "purple"]

turtles = []

next_position = 0

for i in colors:

    temp = i
    i = Turtle(shape="turtle")
    i.color(temp)
    i.penup()
    turtles.append(i)
    

for i in turtles:
    i.goto(-230, -140 + next_position)
    next_position += 60

















screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")



is_game_over = False

while not is_game_over:

    for i in turtles:
        i.forward(random.randint(10, 50))
        distance = i.pos()
        turtle_color = i.color()
        if distance[0] >= 230.0 and user_bet == turtle_color[0]:
            print(f"Winner is {turtle_color[0]}. You won!")
            is_game_over = True
            break
        elif distance[0] >= 230.0 and user_bet != turtle_color[0]:
            print(f"Winner is {turtle_color[0]}. You lost!")
            is_game_over = True
            break

screen.exitonclick()