import random
n=random.randint(1,100)
a=-1
guesses=0
while(a!=n):
 a=int(input("Guess the number: "))
 guesses += 1

 if(a<n):
    print("higher number please ")
    
 elif(a>n):
    print("lower number please")
 if(guesses==7):
   print("GAME OVER")
   break
if(a==n):    
 print(f"you have guessed right in {guesses} attempt")
else:
  print("you can not guess the right number") 
  

