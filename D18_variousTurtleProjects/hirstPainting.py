import turtle
import random

turtle.colormode(255)
myTurtle = turtle.Turtle()
myTurtle.speed('fastest')

colorList = [
    (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
    (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)
]
myTurtle.penup()
myTurtle.hideturtle()
myTurtle.setheading(225)
myTurtle.forward(350)
myTurtle.setheading(0)

numOfDots = 100

for dots in range(1, numOfDots + 1):
    myTurtle.dot(20, random.choice(colorList))
    myTurtle.forward(50)

    if dots % 10 == 0:
        myTurtle.setheading(90)
        myTurtle.forward(50)
        myTurtle.setheading(180)
        myTurtle.forward(500)
        myTurtle.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
