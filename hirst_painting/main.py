import turtle as t

import random

t.colormode(255)

color_template = [(226, 147, 98), (28, 102, 177), (161, 56, 90), (148, 79, 51), (225, 61, 96), (113, 174, 215), (244, 227, 95), (173, 20, 41), 
                  (233, 79, 51), (224, 126, 156), (118, 184, 130), (11, 172, 207), (165, 151, 25), (13, 58, 148), (83, 37, 23), (128, 37, 27), 
                  (37, 129, 78), (42, 192, 160), (14, 39, 92), (129, 238, 190), (244, 162, 151), (235, 162, 181), (100, 101, 186), (127, 214, 239), 
                  (66, 77, 38), (74, 31, 46), (20, 93, 54), (160, 175, 234), (254, 238, 0), (26, 65, 48), (251, 7, 38)]



ada = t.Turtle()
ada.shape()
ada.color()
ada.penup()
ada.setpos(-250,-250)
ada.dot(size=20)
ada.speed("fastest")
ada.hideturtle()

dot_count = 1

while dot_count <= 100:
    for dot_vert in range(10):
        vertical_movement = 50 * dot_vert
        ada.setpos(-250,(-250 + vertical_movement))

        for dot_horz in range(10):
            temp_color = random.choice(color_template)
            ada.pencolor(temp_color)
            ada.dot(size=20)
            dot_count += 1
            ada.forward(50)
            
            

                   












screen = t.Screen()
screen.exitonclick()


