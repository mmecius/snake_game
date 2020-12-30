from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboad
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboad()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

games_is_on = True

while games_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("Nom nom")
        food.refresh()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        games_is_on = False
        scoreboard.game_over()



screen.exitonclick()
