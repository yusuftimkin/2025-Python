from turtle import Turtle

POSITIONS = [(0, 35), (0, 100), (0, 160), (0, 220), (0, 280), (0, 340), (0, 400), (0, -35), (0, -100), (0, -160), (0, -220), (0, -280), (0, -340), (0, -400) ]

class Net():

    def __init__(self):
        self.segments = []
        self.create_line()


    def create_net(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.shapesize(1.2, 0.2)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def create_line(self):
        for position in POSITIONS:
            self.create_net(position)

