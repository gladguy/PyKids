import turtle 

star=turtle.Turtle()

star.shape("turtle")

screen=turtle.Screen()  # Take control of the Turtle Screen
screen.bgcolor("grey")

star.pencolor("red")  # Standards color

for i in range(5): # Star have five sides
  star.forward(100) 
  star.right(144)


childstar = star.clone()
print ("New Star is ready")

screen=turtle.Screen()
screen.bgcolor("yellow")


childstar.pencolor("green")
childstar.forward(-100)

for i in range(5): 
  childstar.forward(100) 
  childstar.right(144)


