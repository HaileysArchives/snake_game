from turtle import Turtle, Screen
from snake import Snake 
from food import Food 
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()    


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

    if snake.head.distance(food) < 15: # distance()
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < - 280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments[1:]: # using slicing with tuple
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    #Detect collision with tail.
    # for segment in snake.segments:
    #     if snake.head.distance() < 10: # 첫 번째 세그먼트가 뱀 머리가 되기 때문에 이것만 작성해서는 즉시 게임이 종료된다. 
    #         game_is_on = False
    #         scoreboard.game_over()

    #if head collides with any segment in the tail:
        #trigger game_over

# using slicing with tuple (튜플에서 슬라이싱 하는 법)
# piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

# print(piano_keys[2:5]) # c d e 
# print(piano_keys[:5]) # a b c d e
# print(piano_keys[2:5:2]) # c e 
# print(piano_keys[::2]) # a c e g
# print(piano_keys[::-1]) # g f e d c b a

# piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

# print(piano_tuple[2:5]) # ('mi', 'fa', 'so')