# Move the snake
from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


segments = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup() 
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1) 
    for seg in segments:
        seg.forward(20)
        # time.sleep(1) # 1s delay

screen.exitonclick()

# 우리가 뱀의 몸을 만들었을 때, 각각의 개별 조각이 생성된 다음 해당 위치로 이동되는 것을 볼 수 있다. 즉 동시에 움직이지 않는다. 

# turtle.tracer(n = None, delay = None)
# turtle.update() => Perform a TurtleScreen update. To be used when tracer is turned off.
# turtle.trace <=> turtle.update()
