
#############################################
def getMarks(subject):
    while True:
        marks = input("Enter your marks for the " + subject + ":")
        if marks.isnumeric():
            break
        else:
            print("You have entered invalid mark, please enter again")

    return int(marks)
#############################################        

student = input("Enter your name :")

print ("Student Name is --> ",student)

while True:
    alphabet_age = input("Enter your age :")
    
    if alphabet_age.isnumeric():
        age = int(alphabet_age)
        print("Student Age is --> ", int(age))
        break
    else:
        print("You have characters in age please re-enter again")
#End of While Loop


getMarks("English")
getMarks("Maths")
getMarks("Computer")        

print("Thank you ", student)
#Outside the While loop









