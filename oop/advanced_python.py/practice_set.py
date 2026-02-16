try:
    with open("1.txt","r") as f:
        print(f.read())
except Exception as e:   
    print(e)
try:
    with open("2.txt","r") as f:
        print(f.read())
except Exception as e:   
    print(e)
try:
    with open("module.py","r") as f:
        print(f.read())
except Exception as e:   
    print(e)
print("thank you") 

l=[1,2,3,4,5,6,7,8]
for i,item in enumerate (l):
    if i==2 or i==4 or i==6:
        print(item)

n=int(input("enter your number: "))
table=[n*i for i in range(1,11)]
print(table)

try:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    print(a/b)
except ZeroDivisionError as v:
    print ("infinite")    

n=int(input("enter a number: "))
table=[n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(f"Table of {n}:{str(table)}\n")