print("MENU")

option1="Add expense"
print(1)
option2="View expenses"
print(2)
option3="Category wise total"
print(3)
option4="EXIT"
print(4)
option1==1
option2==2
option3==3
option4==4

d={"amount" : int(input("Amount")),
   "category" : input("category"),
   "note" : input("note") ,
   "Date" : input("Date") }
Expenses=[d.get("amount")]
n=int(input("Enter user choice: "))

if(n==1):
    L=(input("enter expense: "))
    A=int(input("add expense"))
    
    Expenses.append(A)
    print(Expenses)
    print(d)

elif(n==2):
    print(d.get("amount")),
    print(d.get("category")),
    print(d.get("note")),
    print(d.get("Date"))    
elif(n==3):
    pass
    
elif(n==4):
    print("EXIT")        





    



