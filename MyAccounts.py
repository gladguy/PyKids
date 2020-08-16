f = open("April.txt","a")

expense_date = input("Enter the date :")
expense = input("Enter the Expense details :")
amount = input("Enter the amount :")

f.write(expense_date + "," + expense + "," + str(amount))

f.write("\n") # Line Break

f.close()

f = open("April.txt","r")

print(f.read())

