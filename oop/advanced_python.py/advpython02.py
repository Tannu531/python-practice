from module import myfunc
myfunc()

#global keyword 
a=89
def fun():
    global a #if we dont write this than it prints 3 and 89 but by global it changes the value of a 
    a=3
    print(a)
fun()    
print(a)
l=[3,513,53,40,5]
# index=0
# for item in l:
#  print(f"the item number at index {index} is {item}")
#  index+=1
#This can be simplified using enumerate functions 
for index,item in enumerate(l):
 print(f"the item number at index {index} is {item}")
myList=[1,2,3,4,5,6]
# squaredList=[]
# for item in myList:
#     squaredList.append(item*item)
#this can be simplified as 
squaredList=[i*i for i in myList]
print(squaredList)