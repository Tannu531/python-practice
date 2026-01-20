print("MENU")

1="Add expense"
print(1)
2="View expenses"
print(2)
3="Category wise total"
print(3)
4="EXIT"
print(4)

n=input("Enter user choice: ")
o=n
if(o==1):
    a=int(input("add expense"))
    Expenses=[]
    L=(input("enter new expense: "))
    Expenses.append(L)
    d={"amount" : int(input("Amount")),
   "category" : input("category"),
   "note" : input("note") ,
   "Date" : input("Date") }
    print(a)

elif(o==2):
    t="Date","category","amount","note"    
    print(t)
    
elif(o==3):
    b=int(input(f"amount spend on {"note"}"))
    print(b)
elif(o==4):
    print("EXIT")        





    



