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
list1 = [1, 1.2, 1.5, 1.7, 2, 2.2, 2.5, 2.7, 3, 3.2, 3.5, 3.7, 4]
Rand1 = (random.choice(list1))
list2 = [4, 4.2, 4.5 , 4.7, 5, 5.2 , 5.5, 5.7, 6, 6.2, 6.5, 6.7, 7]
Rand2 = (random.choice(list2))

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