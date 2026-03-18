import webbrowser
import datetime   
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
      print(f"The current time is {hour}:{minute:02d}PM")
   elif(hour==12):
      print("the current time is 12:00 PM")   
   elif(hour==0):
      print("the currect time is 0:00 AM")  
    
   else: 
         
     print(f"The current time is {hour}:{minute:02d}AM ")
def calculator():
   
   n2=input("enter operation: ").lower()
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
   elif(n2=="multiplication"):
      number1=int(input("enter first number: "))
      number2=int(input("enter second number: "))   
      multiplication=number1*number2
      print(multiplication)
   elif(n2=="division"):
      number1=int(input("enter first number: "))
      number2=int(input("enter second number: ")) 
      if(number2==0):
         print("infinity")    
      division=number1/number2
      print(division) 
     
   else:
      print("enter valid operation")      

def showhelp():
    print("available commands are:\n youtube\n time\n google\n calculator\n exit\n")
dict={
    "youtube" :youtube,
    "google" :google,
    "whatsapp":whatsapp,
    "spotify":spotify,
    "github":github,
    "instagram":instagram,
    "calculator":calculator,
    "time":time,
    "help":showhelp
 }    
          
while(True):
 
 n=input("enter your command: ").lower()
 if("hi" in n or "hello" in n or "hey" in n):
     print("hello! how may i help you")
 elif("exit" in n or "bye" in n):
    print("bye bye ! see you soon")
    break
 elif(n in dict):
    dict[n]()
 else:
   print("invalid input")   
 
 
       
