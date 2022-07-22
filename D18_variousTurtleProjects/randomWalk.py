import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
timmyTurtle = Turtle()
timmyTurtle.pensize(12)
def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

randomColor()
turtle.speed('fastest')

colors = ["red", "blue", "green", "brown2", "darkmagenta", "aquamarine3", "gold2"]
angles = [0,90,180,270]

def work():
    timmyTurtle.setheading(random.choice(angles))
    timmyTurtle.pencolor(randomColor())
    timmyTurtle.forward(30)

for i in range(200):
    work()

screen = Screen()
screen.exitonclick()