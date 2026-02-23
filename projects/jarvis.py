import webbrowser
import datetime   

while(True):
 n=input("enter your command: ").lower()
 if("exit" in n or "stop"in n or "bye" in n):
    print("bye bye! will meet next time")
    
    break
 elif("hi" in n or "hello" in n or "hey" in n):
    print("hello! how may i help you")
    
 elif("youtube" in n):
    print("opening youtube")
    
    webbrowser.open("https://www.youtube.com")
    
 elif("google" in n):
    print("opening google")

    webbrowser.open("https://www.google.com")  
 elif("whatsapp" in n):
    print("opening whatsapp")
    
    webbrowser.open("https://web.whatsapp.com")
 elif("github" in n):
    print("opening github")
   
    webbrowser.open("https://github.com")   
 elif("spotify" in n):
    print("opening spotify")
    
    webbrowser.open("https://open.spotify.com")   
 elif("instagram" in n):
    print("opening instagram")

    webbrowser.open("https://www.instagram.com")  
 elif("time" in n):
    
    current=datetime.datetime.now()
    hour=current.hour
    minute=current.minute
    
    if(hour>12):
       hour=hour-12
       
      
    print(f"The current time is {hour}:{minute:02d} ")
 elif("calculator" in n):
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
       

 elif("help" in n):
    print("available commands are:\n youtube\n time\n google\n calculator\n exit\n")
        
         
     
 else:
    print("i dont understand")
      
