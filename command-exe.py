#before running this file make sure that you had the speech_recognition and subprocess modules are installed in your system
import speech_recognition as speech
import subprocess
rec = speech.Recognizer()   
with speech.Microphone() as source:
    print("speak your command :-)")
    aud = rec.listen(source) #here your voice is stored in a variable
    try:
        rec.adjust_for_ambient_noise(source, duration=0.2) 
        t = rec.recognize_google(aud,language="en")         #here your languageof your voice is recognized 
        t = list(t.split(" "))
        if("Notepad" or "notepad" in t):            #here your applications are opend based on your commands
            subprocess.call('notepad.exe')
        elif("Calculator" in t):
            subprocess.call('calc.exe')
        elif("Command " in t or "cmd" in t):
            subprocess.call('cmd.exe')
        elif("Chrome" or "Google" or "google" or "chrome" in t):
            subprocess.call('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
        elif("Firefox" or "Mozilla" or "firefox" in t):
            subprocess.call("C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe")
        print(' '.join(t))           #here your voice command is printed 
    except:
        print("problem occured")
