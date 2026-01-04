a=int(input("enter number: ")) #for writing the table
for i in range(a,10*a+1,a):
   print(i)

l=["harry","sohan","sachin","rahul"] #for greeting people only whose name starts with s
for name in l:
   if(name.startswith("s")):
       print(f"Hello {name}")

n=int(input("enter number: ")) #writing table with while
i=1
while(i<11):
   print(f"{n}*{i}:{n*i}")
   i=i+1

n=int(input("enter your number: "))  #for telling if a number is prime or not
for i in range(2,n):
    if(n%i)==0:
        print("number is not prime ")
        break
        
else:
    print("number is prime")    


n=int(input("enter your number: "))  #for finding the sum of first n natural numbers 
i=1
sum=0
while(i<=n):
    sum=sum+i
    i=i+1
print (sum)

n=int(input("enter number: "))   #for finding factorial
fact=1
for i in range(1,n+1):   #n+1 should be written only then it will work till n
     fact=fact*i
print(fact)    

n=int(input("enter number: "))
for i in range (1,11):
    print(f"{n}*{11-i}={n*(11-i)}") #because here 1,2,3=10,9,8 & all these sum is 11