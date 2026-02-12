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