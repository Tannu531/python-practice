print("MENU")
print("1.Add expense")
print("2.View expenses")
print("3.Category wise total")
print("4.EXIT")
Option1="Add expense"
Option2="View expenses"
Option3="Category wise total"
Option4="EXIT"




d={"amount" : int(input("Amount")),
   "category" : input("category"),
   "note" : input("note") ,
   "Date" : int(input("Date-month-year")) }

Expenses=[]
L=(input("enter new expense: "))
Expenses.append(L)

n=input("Enter user choice: ")

if("user chooses Option1"):
    print(int(input("add expense")))
elif("user chooses option2"):
    a=Date|category|amount|note    
    print(a)
elif("user chooses option3"):
    b=int(input(f"amount spend on {note}"))
    print(b)
else:
    print("EXIT")        



