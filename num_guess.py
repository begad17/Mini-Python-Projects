"""
https://www.youtube.com/watch?v=DLn3jOsNRVE
Generate random number
Count how many tries
"""

#importing this MODULE
import random

#print(random.randrange(start,stop)) DOES NOT INCLUDE THE STOP NUMBER
#if you use .randint it will include that stop number

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range) #converting it from str to int

    if top_range <= 0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please enter a number")
    quit()

r = random.randint(0,top_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Take a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a number")
        continue #brings us back up to the loop

    if user_guess == r:
        print("You got it!")
        break
    elif user_guess > r:
            print("You were above the number.")
    else:
            print("You were below the number.")
        
     
print("You got it in", guesses, "guesses")


