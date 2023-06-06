name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer = input("You are on a dirt road that has come to an end. You can go either left or right. What would way would you like to go? ").lower()

if answer == "left":
    answer = input("You have come to a river. You can either walk around it or swim across it. Type walk to walk across it and swim to swim around it: ")
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid answer. You lose")

elif answer =="right":
    answer = input("You have come to a bridge and it looks wobbly. Do you want to cross it or turn back (cross/back)? ")
    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You tallked to the stranger and they gave you the gold. You win!")
        elif answer =="no":
            print("You ginored the stranger and they are offended so you lose")
        else:
            print("Not a valid answer. You lose")

    else:
        print("Not a valid answer. You lose")

else:
    print("You lose")

print("Thank you for playing the game ", name)
