#using walrus operator
if(n:=len([1,2,3,4,5]))>3:
    print(f"List is too long ({n} elements ,expected <=3)")

#types
n:int=5
name:str="Tannu"

def sum(a:int , b:int)->int:
    return a+b

from typing import List,Tuple,Dict,Union
#list of integers 
numbers:List[int]=[1,2,3,4,5]
#Tuple of a string and an integer
person:Tuple[str,int]=("alice",30)
#Dictionary with string keys and integer values 
scores:Dict[str,int]={"alice":90,"bob":85}
#union type for variables that can hold multiple types 
identifier :Union[int,str]="idt23"

#MATCH CASE 
def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal servor error"
        case _:
            return "unknown status"
print(http_status(200))        
print(http_status(404))  
print(http_status(400))       #random number than output is unknown status

#Dictionary merge and update operators 
dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
merged=dict1|dict2
print(merged)

#exception handling 
try:
    a=int(input("hey,enter a number: "))
    print(a)
except ValueError as v:
    print("heyyy")
    print(v)    
except Exception as e:    
    print(e)
print("Thank you")    

#raising exceptions
a=int(input("enter a number: "))
b=int(input("enter a second number: "))
if(b==0):
    raise ZeroDivisionError("hey our program is not meant for dividing the numbers by zero")
else:
    print(f"the division a/b is {a/b}")
