import os
import pyttsx3
print("Welcome to My world, Sir") 
pyttsx3.speak("Welcome to My world, Sir")
var=1
while var==1 :
 print("what you wan to run sir?")
 pyttsx3.speak("what you wan to run sir?")
 print("For example,you can run:")
 pyttsx3.speak("For example,you can run:")
 
 print("firefox")
 print("chrome") 
 print("windows midea player") 
 print("notepad")
 print("vlc")
 pyttsx3.speak("firefox ,chrome,windows midea player,notepad , vlc")
 
 

 print("Please enter your choice here:" , end=' ')
 pyttsx3.speak("Please enter your choice here:")
 p=input( )

     
 if ("firefox" in p): 
    pyttsx3.speak("alright sir")  
    os.system("firefox")
    
 elif("chrome" in p):
    pyttsx3.speak("alright sir")
    print("alright sir")    
    os.system("chrome")
   
 elif("windows media player" in p):
    pyttsx3.speak("alright sir")
    print("alright sir")    
    os.system("wmplayer")
    
 elif("vlc" in p) or ("VLC" in p):
    pyttsx3.speak("alright sir")
    print("alright sir")    
    os.system("vlc")  
    
 elif ( "notepad" in p) or ("text editor" in p):
    pyttsx3.speak("alright sir")
    print("alroght sir")    
    os.system("notepad")
    
 elif ("thanks"in p) or ("thank you" in p):
    print("your welcome sir, It was a pleasure to help you sir ..")
    pyttsx3.speak("your welcome sir, ...It was a pleasure to help you sir .. ")
   
     
 elif ("close" in p) or ("exit" in p) or ("terminate" in p) or ("turn off" in p) or ("end" in p):
    pyttsx3.speak("alright sir... have a nice day!")
    print("alright sir... have a nice day!")
    exit()
 else:

   print("The executable path for the software you want to run doesn't exist. Please add the full executable path, Directing you to its tutorial(if not directed to the link automatically,use this link) : https://www.youtube.com/watch?v=cQblYrDTphE")
   pyttsx3.speak("The executable path for the software you want to run doesn't exist.please add the full executable path,, directing you to its tutorial") 
   os.system("chrome https://www.youtube.com/watch?v=cQblYrDTphE")
