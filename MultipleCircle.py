import turtle

pet = turtle.Turtle()

screen=turtle.Screen()
screen.setup(500,500) # Size of the Screen

pet.pencolor('green')
pet.pensize(1)

pet.shape('turtle')

n=0   
while n < 7:   #loop for 7 circles
    n=n+1   
    pet.penup()   
    pet.setpos(0,-n*20)   
    pet.pendown()   
    pet.circle(20*n)
    pet.pensize(n)
    print("Value of n=" + str(n));
