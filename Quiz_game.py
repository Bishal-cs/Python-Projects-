print("------------------Welcome To the Quiz Game------------------")
Playing = input("Do you want to play the game? (yes/no): ")

if Playing.lower() != "yes":
    quit()

print("Lets Play the game! Good Luck!")
score = 0

ans = input("1. What is the full form of CPU? ")
if ans.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("2. What is the full form of GPU? ")
if ans.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("3. What is the full form of RAM? ")
if ans.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

ans = input("4. What is the full form of ROM? ")
if ans.lower() == "read only memory":
    print("Correct!")    
    score += 1
else:    
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")