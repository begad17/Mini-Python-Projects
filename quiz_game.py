"""
Ask user several questions
Right answer = a point
"""

print("Welcome to the game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Awesome, let's play!")

score = 0

answer = input("Do you love nani? ").lower()
if answer == "yes":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("Habibi or Batata? ").lower()
if answer == "habibi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Lucky Buns or Village Chicken? ").lower()
if answer == "lucky buns":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Am I your smoothie? ").lower()
if answer == "yes":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
