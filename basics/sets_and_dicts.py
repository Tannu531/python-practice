s={1,5,3,2}
e= s()#prints an empty set ,dont use {} it will create an empty dictionary
s.add("harry") #adds the given element
print(s,type(s))
s.remove(3)  #removes a particular element
print(s)
print(len(s)) #gives length of set
print(s.pop()) 
s.clear()  #empty set
print(s)

s1={22,4,5,21,30,4,5,5}
s2={24,25,5,4,6,9}
print(s1.intersection(s2)) #intersection of s1 and s2 
print(s2.union(s2))     #union of s1 and s2
