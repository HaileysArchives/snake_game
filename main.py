from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create 3 turtles and position them like so: Each turtle should be a white square (default size: 20 x 20)
snake = Turtle()
snake.shape("square")
snake.color("white")
snake_shape = []

def make_snake():
    i = 0
    for snake in range(0,3):
        new_snake = Turtle(shape = "square")
        new_snake.color("white")
        new_snake.goto(x = -20 + i, y = 0)
        i += 20
        snake_shape.append(new_snake)

make_snake()

screen.exitonclick()