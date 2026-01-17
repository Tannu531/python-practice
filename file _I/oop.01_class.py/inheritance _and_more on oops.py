# #single inheritance
# class employee:
#     company="ITC"  #company is a class variable ,(always at the top)
#     name="tannu"   
#     def show(self): #show()=general employee details 
#         print(f"the  name of employee is {self.name} and the company is {self.company}")

# class coder:
#     language="python"
#     def slanguage(self):
#         print(f"my favourite language is {self.language}")

# class programmer(employee,coder):
#     company="ITC infotech"
#     def showlanguage(self): #show language()=programmer specific details 
#         print(f"the name of the employee is {self.name},favourite language is{self.language} and his company is {self.company}")


# #multiple inheritance 
# a=employee()  #a is demo line for showing it can also be used independently.no change if not used 
# b=programmer()

# b.show()    # b inheritance ki power show krne ke lie use hua h .
# b.slanguage()
# b.showlanguage()

# #multilevel inheritance 
# class employee:
#     a=1
# class programmer (employee):
#     b=2
# class manager(programmer):
#     c=3
# o=employee()
# print(o.a)    #prints the a attribute
# #prints(o.b) shows an error as their is no b attribute in employee class
# o=programmer()
# print(o.a,o.b)          
# o=manager()
# print(o.a,o.b,o.c)

# #super()method
# class employee:
#     def __init__(self):
#      print("constructor of employee")
#     a=1
# class programmer (employee):
#     def __init__(self):
#      print("constructor of programmer")
#     b=2
# class manager(programmer):
#     def __init__(self):
#      super().__init__()
#      print("constructor of manager")
#     c=3
# # o=employee()
# # print(o.a)    #prints the a attribute
# # #prints(o.b) shows an error as their is no b attribute in employee class
# # o=programmer()
# # print(o.a,o.b)          
# o=manager()
# print(o.a,o.b,o.c)

#class method
# class employee:
#    a=1
#    @classmethod
#    def show(cls):
#       print(f"the class attribute of a is {cls.a}")
# e=employee()
# e.a=45
# e.show()

#property method and getter,setter
# class employee:
#    a=1
#    @property
#    def name(self):
#       return(f"{self.fname} {self.lname}")
#    @name.setter
#    def name(self,value):
#       self.fname=value.split(" ")[0]
#       self.lname=value.split(" ")[1]
# e=employee()  
# e.name="Harry Khan"
# print(e.fname,e.lname)

class number:
    def __init__(self,n):
        self.n=n
    def __add__(self,num):
        return self.n + num.n

n=number (1)
m=number(2)
print(n+m)        