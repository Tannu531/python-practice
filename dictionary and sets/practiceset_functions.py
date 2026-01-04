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
