class programmer:
    company="microsoft"
    def __init__(self,name,salary):  #keep space after def
        self.name=name
        self.salary=salary   #we dont have to specify salary here
p1=programmer("tannu",120000)  
print(p1.name,p1.salary,p1.company)
p2=programmer("tanuj",11000)     
print(p2.name,p2.salary,p2.company)


class calculator:
    def __init__(self,n):
        self.n=n         #stores the number inside the object
    def square(self):     #defines a method to calculate square
        print(f"the square of the number is {self.n*self.n}")
    def cube(self):
        print(f"the cube of the number is {self.n*self.n*self.n}")   
    def squareroot(self):
        print(f"the squareroot of the number is {self.n**1/2}")   
    @staticmethod
    def greet():
        print ("hello!")      
a=calculator(4)   #a is an object that contains self.n=4
a.greet()
a.square()        #calls the square method for no.4 
a.cube()
a.squareroot()

class abc:
    a="tannu"
o=abc()
print(o.a)      #prints the class attribute bcoz instance attribute is not present
o.a=0           #instance attribute is set
print(o.a)      #prints the instance attribute bcoz instance attribute is present 
print(abc.a)    #prints the class attribute
 
from random import randint   #for importing random no
class Train:
    def __init__(self,trainNo):
        self.trainNo= trainNo
    def book(self,fro,to):
        print(f"ticket is booked in trainNo:{self.trainNo} from {fro} to {to}")  
    def status(self):
        print(f"Train no:{self.trainNo} is running on time")      
    def getfare(self,fro,to):
        print(f"Ticket fare in TrainNo:{self.trainNo} from {fro} to {to} is {randint(222,543)}")    
t=Train(1234)
t.book("Rampur","Delhi")
t.status()
t.getfare("haryana","Chandigarh")



      
