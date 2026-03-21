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
   if(hour>=12):
      print(f"The current time is {hour}:{minute:02d} PM")
   elif(hour<12):
      print(f"The current time is {hour}:{minute:02d}  AM ")
   elif(hour%12==0):
      hour=hour+12
       
   
         
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
    print("available commands are:\n youtube\n whatsapp\n github\n spotify\n instagram\n time\n google\n calculator\n exit\n")
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
    "help":showhelp
 }    
          
while(True):
 n=input("enter your command: ").lower()
 if("hi" in n or "hello" in n or "hey" in n):
     print("hello! how may i help you")
     continue
 elif("exit" in n or "bye" in n):
    print("bye bye ! see you soon")
    break
 for key in dict: 
    if(key in n):
       dict[key]()
       break
 else:
   print("invalid input")   
 
 
       
