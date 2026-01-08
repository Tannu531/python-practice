class Employee:   #language and company are class attributes 
    language="Py"
    company="Microsoft"
Tannu=Employee()
Tannu.name="Tannu" #this is an instance attribute
print(Tannu.name,Tannu.language) 
rohan=Employee()
print(rohan.company,rohan.language) 
Harsh=Employee()  
Harsh.name="Harsh"
print(Harsh.name)

#here name is instance attribute and language and company are class attribute because they directly belong to the class 