import random

user_point = 0
computer_point = 0

options = ["rock", "paper", "scissors"]

while True: 
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_point += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_point += 1

    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_point += 1

    else:
        print("You lost!")
        computer_point += 1

print("You won", user_point, "times.")
print("The computer won", computer_point, "times.")
print("Goodbye!")