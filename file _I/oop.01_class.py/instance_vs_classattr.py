class Employee:   #language and company are class attributes 
    language="Py"
    company="Microsoft"
Tannu=Employee()
Tannu.name="Tannu" #this is an instance attribute
Tannu.language="java"
print(Tannu.name,Tannu.language,Tannu.company)