fruits=[]
f1=input("enter fruit name: ")   #to input 7 fruit names in a list
fruits.append(f1)
f2=input("enter fruit name: ")
fruits.append(f2)
f3=input("enter fruit name: ")
fruits.append(f3)
f4=input("enter fruit name: ")
fruits.append(f4)
f5=input("enter fruit name: ")
fruits.append(f5)
f6=input("enter fruit name: ")
fruits.append(f6)
f7=input("enter fruit name: ")
fruits.append(f7)
print(fruits)

marks=[]
s1=int(input("enter marks: "))  #to input marks in sorted manner ,int is written to change the type from string to int
marks.append(s1)
s2=int(input("enter marks: "))
marks.append(s2)
s3=int(input("enter marks: "))
marks.append(s3)
s4=int(input("enter marks: "))
marks.append(s4)
s5=int(input("enter marks: "))
marks.append(s5)
s6=int(input("enter marks: "))
marks.append(s6)
marks.sort()
print(marks)

a=(24,1,"harry")
a[2]="Tannu"    #tuple can not be changed in python


a=[213,214,33,22]
print(a[0]+a[1]+a[2]+a[3])  #to print the sum of 4 numbers

a=(7,0,8,0,0,9)
print(a.count(0)) #to count number of zeroes 


