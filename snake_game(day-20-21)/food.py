from turtle import Turtle
import random


class Food(Turtle):

    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.color("red")
        self.relocate()

    def relocate(self):
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        self.goto(cor_x, cor_y)



    