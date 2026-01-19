from turtle import Turtle, Screen

ada = Turtle()
ada.shape("turtle")
ada.color("green")

def move_forwards():
    ada.forward(10)

def move_right():
    ada.right(10)
    

def move_left():
    ada.left(10)
    

def move_back():
    ada.backward(10)
    
def clear_screen():
    screen.resetscreen()
    ada.color("green")
    ada.home()


screen = Screen()

screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "d", fun = move_right)
screen.onkey(key = "a", fun = move_left)
screen.onkey(key = "s", fun = move_back)
screen.onkey(key = "c", fun = clear_screen)


screen.exitonclick()