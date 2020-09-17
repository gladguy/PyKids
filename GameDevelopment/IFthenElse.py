x = 10  #Intial
x = input("Enter X value ")

print("Value entered by the user " + str(x))

if(x.isnumeric()): #Explain this We are string to number
    x = int(x)
    if  (x > 85):
        print("First Class")
    elif (x < 85 and x >= 60):
        print("Second Class")
    elif (x < 60 and x >= 35):
        print("Third class")
    else:
        print("Better luck next time")
else:
    print("Please enter your marks in number ")
