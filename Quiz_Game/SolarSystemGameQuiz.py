
print("Welcome to the world of planets and moons! :) ")

playing = input("Do you wish to check your knowledge ? \n")

if playing.lower() != "yes":
    quit()

print("Okay! Let's dive in...\n")

score = 0

answer = input("Which planet is called the evening/morning star?\n")
if answer.capitalize() == "Venus":
    print("Correct\n")
    score += 1
else:
    print("OOPS, Incorrect\n")

answer = input("Which is the planet nearest to the sun?\n")
if answer.capitalize() == "Mercury":
    print("Correct\n")
    score += 1
else:
    print("OOPS, Incorrect\n")

answer = input("Which is the planet farthest from the sun?\n")
if answer.capitalize() == "Neptune":
    print("Correct\n")
    score += 1
else:
    print("OOPS, Incorrect\n")

answer = input("The moon is the Earth’s ____? : \n")
if answer.capitalize() == "Natural satellite":
    print("Correct\n")
    score += 1
else:
    print("OOPS, Incorrect\n")

if score >=3:
    print("Bravo!")
elif score ==2:
    print("Good Job")
else:
    print("Better Luck Next Time!")

print("You got " + str(score) + " number of questions correct. ")
print("And you got " + str((score / 4) * 100) + "%.")
