def ReadAccount(mode): # Mode 1 for Print line 1 
    f = open("April.txt","r")
    cnt = 0
    totalExpense = 0.00
    line = f.readline()
    while line:
        if(mode == 1):
            print(line)
        
        line = f.readline()
        cnt += 1

        # 18/08/2020,Milk,20.00 tokens
        tokens = line.split(",") 
        count = 0
        for token in tokens:
            count = count + 1
            if(count == 3):
                token = token[:-2] #Remove the line break 
                totalExpense = float(token) + totalExpense
        #End of the While
    print ("Your Total Expenses AED " + str(totalExpense))


#Main Program
  

ReadAccount(0) # Print Total Expenses


#Read from the User
expense_date = input("Enter the date (dd/mm/yyyy):")
expense = input("Enter the Expense details :-")
amount = input("Enter the amount AED ")

f = open("April.txt","a")

#Write to the file
f.write(expense_date + "," + expense + "," + str(amount))
f.write("\n") # Line Break
f.close()

#Read the Account File
ReadAccount(1)

