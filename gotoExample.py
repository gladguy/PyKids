import turtle
from random import seed
from random import randint

pet = turtle.Turtle()

pet.shape("turtle")

screen=turtle.Screen()
screen.setup(500,500)

for i in range(10): # 10 Stars
    pet.pencolor("white")
    pet.setpos(randint(-200,200),randint(-200,200))
    # Draw a star
    for j in range(5):
        pet.pencolor("red")
        pet.forward(100)
        pet.right(144)
        
    #Loop end
pet.done()        
    

