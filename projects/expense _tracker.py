print("MENU")

print("1.add expense")
print("2.view expense")
print("3.category wise total")
print("4.exit")


Expenses=[]


while True:
 n=int(input("Enter user choice: "))
 if(n==1):
    
    expense={"amount" : int(input("Amount: ")),
   "category" : input("category: "),
   "note" : input("note: ") ,
   "Date" : input("Date: ")
     }

    Expenses.append(expense)
    print(Expenses)
 
 elif(n==2):
    if not Expenses:    
     print("no expenses added yet,please add an expense first")
    else: 
     for e in Expenses:
      print("amount:",e["amount"]),
      print("category:",e["category"]),
      print("note:",e["note"])
      print("Date:",e["Date"])
      print("------")
 elif(n==3):
     if not Expenses:
      print("No expenses added yet , please add an expense first")  
     else:    
      T=input("user category: ")
      total=0
      for e in Expenses:
       if e["category"].lower()==T.lower():
        total=total+e["amount"]
     print("Total expense for",T,"=",total)    
      

   
 elif(n==4):
    print("EXIT ,Thanks!")  
    break      
 else:
   print("invalid choice enter choice 1-4")




    



