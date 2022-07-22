import random
import turtle

turtle.colormode(255)

timmyTurtle = turtle.Turtle()
timmyTurtle.speed('fastest')


def randomColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


timmyTurtle.circle(100)
for a in range(0, 361, 5):
    timmyTurtle.color(randomColor())
    timmyTurtle.circle(radius=100)
    timmyTurtle.setheading(a)

screen = turtle.Screen()
screen.exitonclick()
