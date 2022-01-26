name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road, it has come to an end you can go left or right, where do you want to go?").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around or swim across. Type 'walk' or 'swim'").lower()

    if answer == "swim":
        print("You swam across but drowned")
    elif answer == "walk":
        print("You got too tired from walking and died")
    else:
        print("Not a valid option.")

elif answer == "right":
    answer = input("You reach a bridge, it is wobbly so do you walk across or go under. Type 'walk' or 'under'").lower()
    
    if answer == "walk":
        print("You fall and die")
    elif answer == "under":
        print("You made it to the end and won!")
    else:
        print("Not a valid option.")
else:
    print("Not a valid option.")

print("Thank you for playing ", name)
