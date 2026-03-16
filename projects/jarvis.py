import webbrowser
import datetime   

def exit():
 if("exit" in n or "bye" in n ):
   print("bye bye !see you soon ")
   break

def youtube():   
   
   print("opening youtube")
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
   print("opening spotify")
   webbrowser.open("https://open.spotify.com")   


def instagram():
   print("opening instagram")
   webbrowser.open("https://www.instagram.com")  


def time():
   
    current=datetime.datetime.now()
    hour=current.hour
    minute=current.minute
    
    if(hour>12):
       hour=hour-12
       
      
    print(f"The current time is {hour}:{minute:02d} ")
def calculator():
   if("calculator" in n):
      n2=input("enter operation: ")
      if(n2=="addition"):
       number1=int(input("first number: "))
       number2=int(input("second number: "))
       addition=number1+number2
       print(addition)
      elif(n2=="subtraction"):
       number1=int(input("first number: "))
       number2=int(input("second number: "))
       subtraction=number1-number2
       print(subtraction)
       

def showhelp():
    print("available commands are:\n youtube\n time\n google\n calculator\n exit\n")
          
while(True):
 
 n=input("enter your command: ").lower()
 
 if("hi" in n or "hello" in n or "hey" in n):
     print("hello! how may i help you")
 if("youtube" in n):
    youtube()
 if("google" in n):
    google()
 if("whatsapp" in n):
    whatsapp()
 if("spotify" in n):
    spotify()
 if("github" in n):
    github()
 if("instagram" in n):
    instagram()
 if("calculator" in n):
    calculator()
 if("time" in n):
    time()
 if("help" in n):
    help()                     

