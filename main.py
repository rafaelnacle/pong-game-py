from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_left = Paddle()
paddle_right = Paddle()

paddle_left.goto(x=-350, y=0)
paddle_right.goto(x=350, y=0)


screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

screen.exitonclick()