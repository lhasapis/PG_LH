print ("What's your name?")
name = input() 
print("What's your favorite sport?")
sport = input().title()

if sport == "Hockey":
    print("Go Rangers!")
elif sport == "Lacrosse":
    print ("Lacrosse is a great sport!")
else:
    print(sport + " sounds fun.")


print("What's your favortite art?")
art = input().title()

if art == "Music":
    print ("Do you play an instrument?")
    instrument = input().title()

    if instrument == "Yes":
        print("Wow! So cool!")
    elif instrument == "No":
            print ("You must be an excallent singer!")
elif art == "Art":
    print ("Do you prefer to draw or paint?")
    drawpaint = input().title()

    if drawpaint == "Draw":
        print("You must be a great artist!")
    if drawpaint == "Paint":
        print("You must be a great artist!")
elif art == "Graphic Arts":
    print ("Computer design is very interesting!")
else:
    print(art + " how fascinating!!")
    
          
          
