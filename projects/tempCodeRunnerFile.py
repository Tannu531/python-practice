def notessaver():
   note=input("Write your notes: ")    
   st=note
   f=open("yournotes.txt","a")
   f.write(st+"\n")
   f.close()
def shownotes():
   f=open("yournotes.txt")
   data=f.read()
   print(data) 
   f.close()