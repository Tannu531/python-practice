
option1= "1.Check if prime"
print(option1)
option2=("2.Find factorial")
print(option2)
option3=("3.Find sum of natural numbers till n")
print(option3)
option4=("4.convert celsius to fahrenheit")
print(option4)
option5=("5.EXIT")
print(option5)
def prime_no(n):
    for i in range(2,n):
     if(n%i==0):
        print("number is not prime")
        break
    else:
      print("number is prime")
    
def factorial(n):
     if(n==0 or n==1):
      return 1
     return n*factorial(n-1)
      
def sum_01(n):
     if(n==1):
      return 1
     return sum_01(n-1)+n


def celsius_to_fahrenheit(c):
   fahrenheit=(c*9/5)+32
   return fahrenheit
o=int
while(o!=5):
   print("MENU")
   o=int(input("choose option 1 to 5: "))
   if(o==1):
    n=int(input("enter a number: "))
    prime_no(n)
    
   elif(o==2):
    n=int(input("enter your number: "))
    print(f"factorial of {n} is: ",factorial(n))
   
   elif(o==3):
    n=int(input("enter your number: "))
    print(f"sum of first{n} natural numbers is: ",sum_01(n))
   
   elif(o==4):
    n=int(input("enter temperature in celsius: "))
    print(f"temperature {n} in fahrenheit is: ",celsius_to_fahrenheit(n))
   
   elif(o==5):
    print("EXIT")

   else:
    print("YOU ARE ENTERING INVALID CHOICE")   



