people_count = 0
while people_count < 5:
    name = input("Enter your name :")
    age  = input("Enter your age ")

    if(age.isnumeric()): 
        if( int(age) < 10):
            print("Sorry ", name , " you are too young for the concert")
        else:
            people_count = people_count + 1
            print("Welcome to the Concert Your Ticket Number is 000"+ str(people_count))
            if(people_count >= 5):
                print("Housefull !")
            
    else:
        print("You have to enter in numbers")
