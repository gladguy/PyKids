import turtle

bob = turtle.Turtle()

bob.shape("turtle")

bob.color("red","yellow")

bob.begin_fill()

input("Please enter")
#This is my Loop
for i in range(5):
    bob.forward(300)
    bob.left(170)


if (i > 2):
    bob.circle(300)



bob.end_fill()
bob.done()
