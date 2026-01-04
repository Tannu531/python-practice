#function definition
def avg():
    a=int(input("enter your number: "))
    b=int(input("enter your number: "))
    c=int(input("enter your number: "))

    average=(a+b+c)/3
    print(average)

avg() #function call,function can be called any number of times
print("thanks")
avg()   

def goodday():
    name=input("enter name: ")
    print(f"good day{name}")
goodday()    

def goodday(name,ending):   #function arguments
    print("Good day ," + name)
    print(ending)
goodday("harry" , "thank you")    
goodday("tanu" ,"thanks")

def goodday(name,ending):   
    print("Good day ," + name)
    print(ending)
    return("finish")       #return gives something back to the program
a=goodday("harry" , "thank you")    
print(a)

def goodday(name,ending="thank you"):
    print(f"goodday{name}")
    print(ending)
goodday("tannu","thanks")  
goodday("harsh")    #prints default value in ending i.e.thankyou because argument is not specified


