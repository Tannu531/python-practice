print("snake=1")
print("gun=0")
print("water=2")
GUN=0
SNAKE=1
WATER=2
l1=[]
l2=[]

while(True):
 n1=int(input("Enter choice for player 1: "))
 n2=int(input("Enter choice for player 2: "))
 
 if(n1==-1 and n2==-1):
    print("EXIT! THANK YOU")
    break
 
 if(n1==SNAKE and n2==WATER):
    print("player 1 wins")
    winner=1
 elif(n1==WATER and n2==GUN):
    print("player 1 wins")
    winner=1
 elif((n1==GUN) and (n2==SNAKE)):
    print("player 1 wins")
    winner=1  
 elif(n1==n2):
    print("withdraw ! try again.")
    winner=0
      
 elif(n1==WATER and n2==SNAKE):
    print("player 2 wins")
    winner=2
 elif(n1==GUN and n2==WATER):
    print("player 2 wins")
    winner=2
 elif(n1==SNAKE and n2==GUN):
    print("player 2 wins") 
    winner=2
 
 else:
    print("invalid choice")
 
 if(winner==1):
    l1.append("win")
 elif(winner==2):
    l2.append("win")   
 print("player 1 score: ",len(l1))
 print("player 2 score is: ",len(l2))
 
