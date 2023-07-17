from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)] # 상수
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup() 
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1): # (start = 2, stop = 0, step = -1) 2 1 0
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

# screen.onkey(snake.up, "Up") # angle: 90
# screen.onkey(snake.down, "Down") # angle: 270
# screen.onkey(snake.left, "Left") # angle: 180 
# screen.onkey(snake.right, "Right") # angle: 0
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        # self.segments[0].setheading(90)
        # self.segments[0].forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        # self.segments[0].setheading(270)
        # self.segments[0].forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        # self.segments[0].setheading(180)
        # self.segments[0].forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        # self.segments[0].setheading(0)
        # self.segments[0].forward(MOVE_DISTANCE)