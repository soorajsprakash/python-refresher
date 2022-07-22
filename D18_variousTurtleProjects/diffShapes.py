import random
from turtle import Turtle, Screen

timmyTurtle = Turtle()
timmyTurtle.pensize(12)

colors = ["red", "blue", "green", "brown2", "darkmagenta", "aquamarine3", "gold2"]
currentSide = 3

def draw():
    angleNum = 360 / currentSide
    timmyTurtle.pencolor(random.choice(colors))
    for i in range(currentSide):
        timmyTurtle.forward(100)
        timmyTurtle.right(angleNum)

for i in range(3,11):
    draw()
    currentSide += 1


screen = Screen()
screen.exitonclick()
