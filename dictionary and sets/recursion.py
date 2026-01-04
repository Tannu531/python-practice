def factorial(n):
    if(n==0 or n==1):
        return 1     #It sends 1 back to the place where the function was called.
    return n*factorial(n-1)
n=int(input("enter a number: "))
print(f"factorial of a number is:{factorial(n)}")  #calling of function