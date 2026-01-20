from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake =  Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False

while not is_game_over:
    screen.update()
    time.sleep(0.1) 
    snake.move()

    if snake.head.distance(food) < 15:
        food.relocate()
        snake.new_snake()
        scoreboard.score_write()

        
    
    for seg in snake.segments[1:]:
        if seg.distance(snake.head) < 15:
            is_game_over = True
            scoreboard.game_over()

    if -295 > snake.head.xcor() or snake.head.xcor() > 295 or -295 > snake.head.ycor() or snake.head.ycor() > 295:
        is_game_over = True
        scoreboard.game_over()
       

screen.exitonclick()