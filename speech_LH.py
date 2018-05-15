import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What's shakin bacon")

answer = pg.prompt("Enter your current mood below.")

if answer == "happy":
    speak.Speak("Same LOL because I'm playing Fortnite.")

elif answer == "sad":
    speak.Speak("Oh no! Eat some Ice Cream! That always helps!")
    
elif answer == "vine":
    speak.Speak("Look at all those chickens!")

elif answer == "tired":
    speak.Speak("Well get some sleep you ding dong.")

elif answer == "I'm vegan":
    speak.speak("Fine then what's shakin tofu bacon!")

speak.speak("What do you want to eat?")

food = pg.prompt("Enter food below")

speak.speak("Ok, let's go look for some recipe's.")

wb.open("https://www.youtube.com/results?search_query=" + food)
    
    
