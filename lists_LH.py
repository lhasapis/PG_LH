name = "Lindsay"

friendscharecters = ["Rachel","Ross","Monica","Chandler","Joey","Phoebe","Janice"]

for i in friendscharecters:
    if i == "Janice":
        print(i + " is annoying!")
    elif i == "Rachel":
        print(i + " has great style!")
    elif i == "Ross":
        print(i + " likes dinasours!")
    elif i == "Monica":
        print(i + " cleans everything!")
    elif i == "Chandler":
        print(i + " loves to make jokes!")
    elif i == "Joey":
        print(i + " loves to eat!")
    elif i == "Phoebe":
        print(i + " loves to sing")

 friendscharecters = []

 while True:
     print("Who's your favorite charecter from friends? Type 'end' to quit.")
     answer = input()
     if answer == "end":
         break
        else:
            friendscharecters.append(answer)

for i in friendscharecters:
    print("One of your favorite friends charecters is " + i)



              
              
 subjects = ["English","Math","History","Science"]

print("Hello " + name)

for i in subjects:
    print("One of my subjects is " + i)
    

