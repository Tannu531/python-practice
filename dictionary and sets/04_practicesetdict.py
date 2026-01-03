words={
    "madad":"help",
    "accha":"good",
    "shukriya":"thnks"
}
word=input("Enter the word you want meaning of: ")
print(words[word])

s=set()                   #at first create an empty set
n=input("enter number: ")
s.add(int(n))            #int is written so that input is a integer not string 
n=input("enter number: ")
s.add(int(n))
n=input("enter number: ")
s.add(int(n))
n=input("enter number: ")
s.add(int(n))
n=input("enter number: ")
s.add(int(n))
n=input("enter number: ")
s.add(int(n))
n=input("enter number: ")
s.add(int(n))
n=input("enter number: ")
s.add(int(n))
print(s)


s={18,"18"}         #yes we can store 18 as integer and string in the set 
print(s)


s=set()
s.add(20)        #length of the set will be 2 because in python 2.0=2
s.add(20.0)
s.add('20')
print(len(s))

s={}               #type is dictionary
print(type(s))

d={}
name=input("enter name : ")
lang=input("enter favourite language: ")
d.update({name:lang})          #dont use add function in this thats in set only 
name=input("enter name : ")
lang=input("enter favourite language: ")
d.update({name:lang})
name=input("enter name : ")
lang=input("enter favourite language: ")
d.update({name:lang})
name=input("enter name : ")
lang=input("enter favourite language: ")
d.update({name:lang})
print(d)



