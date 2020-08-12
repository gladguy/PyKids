import turtle

#---------------------------------
def drawCircle(size,turtle):
    turtle.pendown()
    turtle.circle(size)
    turtle.penup()
#----------------------------------
def drawStar(size,turtle):
    turtle.pendown()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.penup()
#---------------------------------
def drawSquare(size,turtle):
    turtle.pendown()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()
#---------------------------------
def drawRectangle(height,width,turtle):
    turtle.pendown()

    turtle.forward(width)
    turtle.right(90)

    turtle.forward(height)
    turtle.right(90)

    turtle.forward(width)
    turtle.right(90)
    
    turtle.forward(height)
    turtle.right(90)
    turtle.penup()
#---------------------------------    

bob = turtle.Turtle()
while True:
    print("1 for Circle")
    print("2 for Square")
    print("3 for Star")
    print("4 for Rectangle")
    shape = input("Enter your choice")
    bob.penup()
    bob.goto(100,100)   
    if shape.isnumeric():
        if (int(shape) == 1):
            drawCircle(100,bob)
        elif (int(shape) == 2):
            drawSquare(100,bob)
        elif (int(shape) == 3):
            drawStar(100,bob)
        elif (int(shape) == 4):
            drawRectangle(100,150,bob)
            
        




