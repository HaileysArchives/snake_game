from turtle import Turtle, Screen
from snake import Snake 
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen() 
screen.onkey(snake.up, "Up") # angle: 90
screen.onkey(snake.down, "Down") # angle: 270
screen.onkey(snake.left, "Left") # angle: 180 
screen.onkey(snake.right, "Right") # angle: 0

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()