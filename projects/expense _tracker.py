print("MENU")


option1="Add expense"
print("1.add expense")
option2="View expenses"
print("2.view expense")
option3="Category wise total"
print("3.category wise total")
option4="EXIT"
print("4.exit")

d={}
Expenses=[]

while True:
 n=int(input("Enter user choice: "))
 if(n==1):
    
    d1={"amount" : int(input("Amount")),
   "category" : input("category"),
   "note" : input("note") ,
   "Date" : input("Date") }

    Expenses.append(d1)
    print(Expenses)
    

 elif(n==2):
    for d in Expenses:
     print(d.get("amount")),
     print(d.get("category")),
     print(d.get("note")),
     print(d.get("Date"))    
 elif(n==3):
    T=input("user category")
    total=0
    for e in Expenses:
      if e["category"]==T:
        total=total+["amount"]
        print(total)
      

   
 elif(n==4):
    print("EXIT ,Thanks!")  
    break      





    



