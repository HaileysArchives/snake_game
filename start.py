# Building the famous Snake Game

# Break down the problem.
# 1. Create a snake body (make a 3 squares)
# 2. How to move the snake 
# 3. control the snake using keybord.

# 4. detet collision with food. => food will be random location
# 5. create a scoreboard 
# 6. detect collision with wall => end game (game over show up the screen.)
# 7. detect ccllision with tail. (when the snake's head hits any part of the body of the snake, then it's done)

# 1. Create 3 turtles and position them like so: Each turtle should be a white square (default size: 20 x 20)
from turtle import Turtle, Screen

segment_1 = Turtle("square")
segment_1.color("white")

segment_2 = Turtle("square")
segment_2.color("white")
segment_2.goto(x = -20, y = 0)

segment_3 = Turtle("square")
segment_3.color("white")
segment_3.goto(x = +20, y = 0)
 
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


