print ("Welcome")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Great! Let's play: ")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "cpu":
    print("Correct! Good Job!")
    score += 1
else:
    print("Incorrect")


answer = input("Is Bill Gates evil? ")
if answer.lower() == "yes":
    print("Correct! Good Job!")
    score += 1
else:
    print("Incorrect")

answer = input("Did Epstein hang himself? ")
if answer.lower() == "no":
    print("Correct! Good Job!")
    score += 1
else:
    print("Incorrect")

answer = input("How many times did Bill Clinton visit Epstein Island? ")
if answer.lower() == "27":
    print("Correct! The pervert visited 27 times!!")
    score += 1
else:
    print("Incorrect")
  
print("You got " + str(score) +  " questions correct")
print("Which gives you " + str((score/4) * 100) +  "%")