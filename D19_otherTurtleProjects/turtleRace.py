from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
yPos = [-100, -60, -20, 20, 60, 100]
turtleList = []
notEnd = True

for i in range(6):
    myTurtle = Turtle(shape="turtle")
    myTurtle.penup()
    myTurtle.color(colours[i])
    myTurtle.goto(-220, yPos[i])
    turtleList.append(myTurtle)

while notEnd:
    for each in turtleList:
        if each.xcor() < 230:
            movement = random.choice(range(0, 15))
            each.forward(movement)
        else:
            notEnd = False
            winningColour = each.pencolor()
            if winningColour == bet:
                print(f"You've WON. The {winningColour} turtle is the winner.")
            else:
                print(f"You've LOST. The {winningColour} turtle is the winner.")


screen.exitonclick()
