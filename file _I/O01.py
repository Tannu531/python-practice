f=open("file.txt")#reading in a file
data=f.read()
print (data)
f.close()

st="everything will be fine" #writing in a file
f=open("my file.txt","a")
f.write(st)
f.close()

f=open("file.txt")
lines=f.readlines()
print(lines,type(lines))
f.close()

f=open("file.txt")
line1=f.readline()
print(line1,type(line1))
line2=f.readline()
print(line2,type(line2))
line3=f.readline()
print(line3,type(line3))
line4=f.readline()
print(line4,type(line4))
line5=f.readline()
print(line5,type(line5))
line5=f.readline()
print(line5=="")
f.close()

 #upper code can be also written as
f=open("file.txt")
line=f.readline()
while(line!=""):
    print(line)
    line = f.readline()
f.close()    


with open("file.txt","r") as f:   #open and closes the file automatically
    text=f.read()
    print(text)

#upper code is same as
# f=open("file.txt")
# print(f.read())
# f.close()    