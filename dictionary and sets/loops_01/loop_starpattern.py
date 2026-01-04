n=int(input("enter a number: "))  #printing a star pattern
for i in range(1,n+1):   
    print(" "*(n-i),end=" ") #print spaces if we have to print 5 rows than (5-1) it prints 4 spaces in first row
    print("*" * (2*i-1),end=" ")#print stars in odd pattern, in 1 row it will prints(2*1-1),then next row 4-1
    print(" ")              

##used this empty print to print a new line after completeing one line    
##used end to print in the same line otherwise after every print it moves to new line

n=int(input("enter a number: ")) 
for i in range(1,n+1):   
    print("*" * (i))             

n=int(input("enter a number: ")) 
for i in range(1,n+1):   
    if(i==1 or i==n):
        print("*"*n,end="")#if we do not write end then there will be 2 rows gap bcoz of emptyprint
    else:
        print("*",end="")
        print(" "*(n-2),end="")#n-2 because only 2 stars prints here so 5-2=3 spaces
        print("*",end="")
    print("")
    
       