class employee:
    language="python"
    salary="1200000"

    def getInfo(self):
        print(f"the language is{self.language}.the salary is{self.salary}")
    @staticmethod    #decorator to mark greet as a static method
    def greet():
        print("good morning")    

tannu=employee()
tannu.greet()
tannu.getInfo() #this can also be written as employee.getInfo(tannu)   

# __init__ (known as constructor)
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1=student("tanu",19)
s2=student("harry",25)
print(s1.name,s1.age)
print(s2.name,s2.age)        