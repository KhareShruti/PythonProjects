import random

user_score = 0
computer_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Quit: \n").lower()
    if user_input == "quit":
        break

    if user_input not in options:
        continue

    random_num = random.randint(0, 2)
    computer_picks = options[random_num]
    print("Computer picked", computer_picks + ".")

    if user_input == "paper" and computer_picks == "rock":
        print("You won. \n")
        user_score += 1

    elif user_input == "scissors" and computer_picks == "paper":
        print("You won. \n")
        user_score += 1

    elif user_input == "rock" and computer_picks == "scissors":
        print("You won. \n")
        user_score += 1

    elif user_input == computer_picks:
        print("Its a draw. \n")

    else:
        print("You lost! \n")
        computer_score += 1
        print("Do you wanna play more : Y or N ? \n")
        ans = input().lower
        if ans == 'n':
            break

print("You won", user_score, " times. \n")
print("The Computer won", computer_score, " times.\n")
print("Thanks for playing, See you in next game...\n")
