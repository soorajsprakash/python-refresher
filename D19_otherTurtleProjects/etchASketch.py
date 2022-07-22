from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def moveFwd():
    tim.forward(10)

def moveBwd():
    tim.back(10)

def right():
    tim.right(15)

def left():
    tim.left(15)

def clearScreen():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=moveFwd)
screen.onkey(key="s", fun=moveBwd)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clearScreen)

screen.exitonclick()
