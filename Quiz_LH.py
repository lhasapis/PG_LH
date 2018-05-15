import pyautogui as pg
import time
import webbrowser



# Set points to zero at start
points=0


# Question Goes here
answer = pg.prompt(
"""
What would you rather do?
a)Go on a hike
b)Watch a movie
c)Go swimming in the ocean

"""
    )

# Tells player their points 
pg.alert("You choose " + answer)

if answer == "a":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "b":
    pg.alert("You gain 2 points")
    points += 2 
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3


# Question Goes here
answer = pg.prompt(
"""
What describes your personality best?
a)Adventurous and loves exploring
b)Comical and loves relaxing
c)Bubbly and seeks fun

"""
    )

# Tells player their points 
pg.alert("You choose " + answer)

if answer == "a":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "b":
    pg.alert("You gain 2 points")
    points += 2 
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3


# Question Goes here
answer = pg.prompt(
"""
What flavors do you like best?
a)Sweet and salty
b)Cookie dough and vanillia
c)Crunchy and Carmel

"""
    )

# Tells player their points 
pg.alert("You choose " + answer)

if answer == "a":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "b":
    pg.alert("You gain 2 points")
    points += 2  
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3

# Question Goes here
answer = pg.prompt(
"""
What's you favorite type of animal?
a)Something fast and ferocious
b)Something cute and cuddly
c)Something that lives under the sea

"""
    )

# Tells player their points 
pg.alert("You choose " + answer)

if answer == "a":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "b":
    pg.alert("You gain 2 points")
    points += 2  
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3

    # Question Goes here
answer = pg.prompt(
"""
What would you rather eat?
a)Caramel
b)Cookie dough
c)S'more's

"""
    )

# Tells player their points 
pg.alert("You choose " + answer)

if answer == "a":
    pg.alert("You gain 1 point")
    points += 1
elif answer == "b":
    pg.alert("You gain 2 points")
    points += 2 
elif answer == "c":
    pg.alert("You gain 3 points")
    points += 3

# END OF SURVEY
pg.alert("You got a total of " + str(points) + " points ")
pg.alert("Ok, here's your Ben and Jerry's Ice cream flavor....")

#Rocky Road
if points <= 6:
    pg.alert("You are Rocky Road-ish!")
    webbrowser.open("http://1.bp.blogspot.com/-_CfYlIixaBM/UDkbusdeaSI/AAAAAAAAAB0/7d3p9Hihk24/s1600/02.JPG")

#Tonight Dough
elif points <=10 and points >=7:
    pg.alert("You are the Tonight Dough!")
    webbrowser.open("https://www.benjerry.com/files/live/sites/systemsite/files/flavors/flavors-redesign-details-2016/ecommerce-assets/pints/Tonight_Dough_1_desktop.jpg")

#Phish Food
elif points <=15 and points >=11:
    pg.alert("You are Phish Food!")
    webbrowser.open("https://www.benjerry.com/files/live/sites/systemsite/files/flavors/flavors-redesign-details-2016/ecommerce-assets/pints/Phish_Food_3_desktop.jpg")










