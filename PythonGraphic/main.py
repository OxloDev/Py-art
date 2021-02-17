import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

#sets backround and pen color
s.bgcolor("black")
t.pencolor("white")

#declares Variables
Var1 = 0
Var2 = 0 

#generates random numbers
Rand1 = random.randint(1, 4)
Rand2 = random.randint(4, 7)

t.speed(0)
t.penup()

#sets pen location
t.goto(0,200)
t.pendown()

#draws until Var2 = 210
while True:
    t.forward(Var1)
    t.right(Var2)
    Var1+=Rand2
    Var2+=Rand1
    if Var2 ==210:
        break
    t.hideturtle()

turtle.done()
