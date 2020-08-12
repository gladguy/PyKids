import turtle

bob = turtle.Turtle()

bob.shape("turtle")
bob.color("red")

"""
Square.
Arrow.
Circle.
Turtle.
Triangle.
Classic.
"""

csize=10 

while (csize < 110):    # This is a while loop
   bob.circle(csize)    # Now my drawing a circle
   csize = csize + 10   
   bob.forward(10)      


