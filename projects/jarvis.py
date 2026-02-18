import webbrowser
n=input("enter your command: ")
import pyttsx3
object=pyttsx3.init()


if ("youtube" in n):
    object.say("opening youtube")
    object.run()
    open ("youtube")
elif("google" in n):
    object.say("opening google")
    object.run()
    open ("google")    
else:
    print("i dont understand")    
