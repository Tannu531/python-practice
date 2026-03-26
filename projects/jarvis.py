import webbrowser
import datetime   
def youtube():   
   print("yaa sure,opening youtube")
   webbrowser.open("https://www.youtube.com")
       
def google():
   print("opening google")
   webbrowser.open("https://www.google.com")  

def whatsapp():
   print("opening whatsapp")
   webbrowser.open("https://web.whatsapp.com")

def github():
   print("opening github")
   webbrowser.open("https://github.com")   

def spotify():
   print("spotify is here!Listen to your fav music")
   webbrowser.open("https://open.spotify.com")   

def instagram():
   print("opening instagram")
   webbrowser.open("https://www.instagram.com")  

def time():
   current=datetime.datetime.now()
   hour=current.hour
   minute=current.minute
   if(hour>=12):
      a="PM"
   elif(hour<12):
      a="AM"
   if(hour%12==0):
      hour=12
   elif(hour%12!=0):
      hour=hour%12   

   print(f"The current time is {hour}:{minute:02d} {a}")      
       
   
         
def calculator():
   print("Available operations are:\n Addition\n Subtraction\n Multiplication\n Division\n")
   print("Type exit to go back")
   while(True):
    
    n2=input("enter operation: ").lower()
    if(n2=="exit"):
       break  
    
    try:
      number1=int(input("first number: ")) 
      number2=int(input("second number: "))
    except:
      if(ValueError):
       print("not correct integer,please retry!")
       continue
    if(n2=="addition" or n2=="add" or n2=="+"):
       addition=number1+number2
       print(f"Result is {addition}")
    elif(n2=="subtraction"or n2=="minus" or n2=="-"):
       subtraction=number1-number2
       print(f"Result is {subtraction}")  
    elif(n2=="multiplication"or n2=="multiply" or n2=="*"):
       multiplication=number1*number2
       print(f"Result is {multiplication}")
    elif(n2=="division" or n2=="divide" or n2=="/"):
      if(number2==0):
        print("cannot divide by 0")
        continue
      else:
          division=number1/number2
          print(f"Result is {division}")   
    else:
       print("Enter valid operation")  

def showhelp():
    print("available commands are:\n youtube:opens youtube\n whatsapp:opens whatsapp\n github:opens github\n spotify:open spotify \n instagram:opens insta\n time:tells current time\n google:google will be opened \n calculator:you can use calculator\n exit:type it for exit\n notessaver:for writing notes\n shownotes:show you the notes\n search:to search something")
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
def search():
   S=input("Please tell us what do you want to search: ")
   webbrowser.open(f"https://www.bing.com/search?q={S}")   
dict={
    "youtube" :youtube,
    "yt":youtube,
    "google" :google,
    "whatsapp":whatsapp,
    "spotify":spotify,
    "github":github,
    "instagram":instagram,
    "insta":instagram,
    "calculator":calculator,
    "calculate":calculator,
    "time":time,
    "help":showhelp,
    "notes":notessaver,
    "shownotes":shownotes,
    "search":search
 }    
      

   
          
while(True):
 n=input("enter your command: ").lower()
 if("hi" in n or "hello" in n or "hey" in n):
     print("hello! how may i help you")
     continue
 elif("kaise ho" in n or "how are you" in n or "suna" in n):
    print("m bdiya ,tu suna kya haal chaal")
    continue
 elif("exit" in n or "bye" in n):
    print("Bye Bye!! Have a good day ji")
    break
 
 for key in dict: 
    if(key in n):
       dict[key]()
       break
 
 else:
   print("It looks like you are writing something wrong !")
   print("your input does not match with our commands, Below is the guide for commands")
   showhelp()
 
   

 
       
