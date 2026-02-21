import webbrowser
import pyttsx3
object=pyttsx3.init()
object.say("hello, how can i help you ")
object.runAndWait()
while(True):
 n=input("enter your command: ").lower()
 if("exit" in n or "stop"in n or "bye" in n):
    object.say("goodbye")
    object.runAndWait()
    break
 elif("youtube" in n):
    object.say("opening youtube")
    object.runAndWait()
    webbrowser.open("https://www.youtube.com")
    
 elif("google" in n):
    object.say("opening google")
    object.runAndWait()
    webbrowser.open("https://www.google.com")  
 elif("whatsapp" in n):
    object.say("opening whatsapp")   
    object.runAndWait()
    webbrowser.open("https://web.whatsapp.com")
 elif("github" in n):
    object.say("opening github")   
    object.runAndWait()
    webbrowser.open("https://github.com")   
 elif("spotify" in n):
    object.say("opening spotify")   
    object.runAndWait()
    webbrowser.open("https://open.spotify.com")   
 elif("instagram" in n):
    object.say("opening instagram")   
    object.runAndWait()
    webbrowser.open("https://www.instagram.com")  
 elif("time" in n):
    pass
              
   
 else:
    object.say("i dont understand")    
