# #using walrus operator
# if(n:=len([1,2,3,4,5]))>3:
#     print(f"List is too long ({n} elements ,expected <=3)")

# #types
# n:int=5
# name:str="Tannu"

# def sum(a:int , b:int)->int:
#     return a+b

# from typing import List,Tuple,Dict,Union
# #list of integers 
# numbers:List[int]=[1,2,3,4,5]
# #Tuple of a string and an integer
# person:Tuple[str,int]=("alice",30)
# #Dictionary with string keys and integer values 
# scores:Dict[str,int]={"alice":90,"bob":85}
# #union type for variables that can hold multiple types 
# identifier :Union[int,str]="idt23"

# MATCH CASE 
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

    

