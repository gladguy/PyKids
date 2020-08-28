print("Hi i am a turtle and I can draw many shapes")
import turtle

    
def circle(radius,bob):
    bob.pendown()
    bob.circle(radius)
    bob.penup()
def star(bob):
    bob.pendown()
    for i in range(5):
        bob.forward(100)
        bob.right(144)
    bob.penup()
def square(bob):
    bob.pendown()
    for i in range(4):
        bob.forward(100)
        bob.right(90)
    bob.penup()
def pentagon(bob):
    bob.pendown()
    for i in range(5):
        bob.forward(100)
        bob.right(72)
    bob.penup()
def hexagon(bob):
     bob.pendown()
     for i in range(6):
        bob.forward(100)
        bob.right(60)     
     bob.penup()
def octagon(bob):
     bob.pendown()
     for i in range(8):
        bob.forward(100)
        bob.right(45)     
     bob.penup()
def decagon(bob):
    bob.pendown()
    for i in range(8):
        bob.forward(100)
        bob.right(36)     
    bob.penup()
def tangentialcircle(bob):
     bob.pendown()
     for i in range(10):
         bob.circle(10*i)
     bob.penup()
def triangle(bob):
     bob.pendown()
     for i in range(2):
         bob.forward(100)
         bob.left(120)
     bob.forward(100)
     bob.penup()
    
    
    
        
         
    

    
    

pet=turtle.Turtle()
pet.shape("turtle")
screen=turtle.Screen()
screen.bgcolor("Red")
penSize=int(input("Enter the pen size of turtle"))
pet.pensize(penSize)
print("What shape you want turtle to draw?")
print("Click 1 for circle")
print("Click 2 for star")
print("Click 3 for square")
print("Click 4 for pentagon")
print("Click 5 for hexagon")
print("Click 6 for octagon")
print("Click 7 for decagon")
print("Click 8 for tangential circle")
print("Click 9 for triangle")
option=int(input("Enter the option:"))
if option in(1,2,3,4,5,6,7,8):
  if (option==1):
           sizeradius=int(input("Enter the radius size:"))
           circle(sizeradius,pet)
  elif(option==2):
           star(pet)
  elif(option==3):
           square(pet)
  elif(option==4):
           pentagon(pet)
  elif(option==5):
           hexagon(pet)
  elif(option==6):
           octagon(pet)
  elif(option==7):
           decagon(pet)
  elif(option==8):
           tangentialcircle(pet)
elif(option==9):
           triangle(pet)
else:
    print("Please enter valid number")


           
           
    
    
           
