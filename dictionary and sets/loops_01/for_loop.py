for i in range (4):   #prints from 0 to 3
    print(i)
l=[2,4,5,445,324,"tannu"]  #prints every element of l
for i in l:
    print(i)    
t=(2,4,5,66)    #can read all elements of t
for i in t:
    print(i)
for i in range(5,50,5):   #same as string slicing 
    print(i)   

n="tannu"
for i in n:     #printing characters one by one 
    print(i)    

l=[1,2,3,4]
for i in l:
    print(i)
else:
    print("done")  #this is printed when the loop exhausts    

for i in range(10):
    if(i==5):
        break    #stops at 4
    print(i)

for i in range(2,7):
    print(i)
    if(i==5):     #stops at 5
        break


for i in range(10):
    if(i==5):
        continue   #skips the iteration
    print(i)

