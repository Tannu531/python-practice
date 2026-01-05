def greatestnumber(a,b,c): #a,b,c are parameters this function will receive 3 no from outside  
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b 
    else:
        return c 
a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number: ")) 
print("greatest number is : ",greatestnumber(a,b,c))

def conversion(fahrenheit): #put fahrenheit tells function depends on a temperature value that will be passed in when it is called.
    celsius=5*(fahrenheit-32)/9
    return celsius
fahrenheit=int(input("enter temperature: "))
print("temperature is: ",conversion(fahrenheit)) #after comma we have not written celsius bcoz it only lie inside funtion

print("a")
print("b")
print("c",end="") #end prevents new line at the end 
print("d",end="")

def sum(n):        #for finding sum of n natural numbers
    if(n==1):      #writing base condition is important
        return 1
    return sum(n-1)+n
n=int(input("enter your number: "))
print("sum of n natural numbers is: ",sum(n)) #calling the function

def star(n):
    if(n==0):     #base condition,is there are 0 stars to print stop evrything
        return 
    print ("*"*n) #before print=increasing
    star(n-1)     #recursive call(after printing this line print pattern for 1 smaller no.)

star(5)

def pattern(n):  #for reversing the order 
    if(n==0):
        return
    pattern(n-1)
    print("*"*n) #after print =decreasing
pattern(4)    

def inch_to_cm(inch):
    return inch*2.54
n=int(input("enter value in inches: "))
print(f"the value in cm is{inch_to_cm(n)}")

def rem(l,word):  #l=original list and word is word to remove 
    n=[]          #new empty list
    for item in l:
        if not(item==word):
            n.append(item.strip(word))#if item=="an"skip it else keep it 
    return n      #Give this new list back to whoever called the function
l=["harrry","rohan","shubh","an"]
print(rem(l,"an"))            

def table(n):
    for i in range(1,11):
     print(f"{n}*{i}={n*i}")
table(2)    
