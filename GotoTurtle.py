import turtle
from random import randint

t1 = turtle.Turtle()

t1.shape('turtle')
t1.penup()

for i in range(5):
    t1.goto(randint(-100,0),randint(0,100))

turtle.done()
