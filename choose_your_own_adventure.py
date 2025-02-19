name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    ans = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

    if ans == "swim":
        print("You swam across and were eaten by an alligator.")

    elif ans == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print("Not a Valid Option!. You lose!")

elif answer == "right":
    ans = input("You come to a bridge, it looks like it can break, do you want to cross or Back(cross/back)? ").lower() 

    if ans == "back":
        print("You go back and lose.")

    elif ans == "cross":
        ans = input("You cross the bridge and meet a stranger. Do you want to talk to them(yes/no)? ")

        if ans == "yes":
            print("You talk to the stranger and they give you gold. You win!")

        elif ans == "no":
            print("You ignore the stranger and they are offended and you lose.")

        else:
            print("Not a Valid Option!. You lose!")
else:
    print("You need to choose left or right!")