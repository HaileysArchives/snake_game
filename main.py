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
    screen.update() # update 함수를 넣으면 그동안 실행되었던 코드들이 스크린창에 업데이트 되는 효과를 볼 수 있다.
    time.sleep(0.1) 

    snake.move()