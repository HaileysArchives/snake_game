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

    # How to move snake? => 두 번째 사각형이 첫 번째 사각형이 있던 위치로 가고, 마지막 사각형이 두 번째 사각형의 위치로 가는 형식
    for seg_num in range(len(segments) - 1, 0, -1): # (start = 2, stop = 0, step = -1) 2 1 0
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)
    segments[0].left(90)


 
# segments[0].left(90) => snake_segment가 연결되지 않아 이상한 동작 발생

screen.exitonclick()

# 우리가 뱀의 몸을 만들었을 때, 각각의 개별 조각이 생성된 다음 해당 위치로 이동되는 것을 볼 수 있다. 즉 동시에 움직이지 않는다. 

# turtle.tracer(n = None, delay = None)
# turtle.update() => Perform a TurtleScreen update. To be used when tracer is turned off.
# turtle.trace <=> turtle.update()
