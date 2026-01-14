def prime_no(n):
    for i in range(2,n):
     if(n==0 or n==1):
        return
     elif(n%i==0):
        print("number is not prime")
        break
     else: 
        print("number is prime")  
n=int(input("enter your number: "))
print=(f"sum of {n} natural numbers is: ",prime_no(n))    
