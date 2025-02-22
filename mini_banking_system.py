from datetime import date,time

print("----welcome to your bank account----")
x = int(input("Enter your Secret Pin: "))

# Enter Your name 
name = "Bishal Das"
# Enter your secret pin to access your account
password = 1234

# options = ["Check Balance", "Widraw", "Deposit"]

def Check_Bal():
    with open("Passbook.txt", "r") as f:
        f.readline()

def Widraw_bal():
    Widraw_amount = 123456
    print(Widraw_amount, "Rs.")

def Deposit():
    current_bal = 100000000
    add_bal = 5000000
    total = current_bal + add_bal
    print("Your current Bal", current_bal, "+" "add money", add_bal, "\n Total bal.", total)

# def your_bank():

#     choose = options[choise]
#     print(choose)
#     # with open("Passbook.txt", "a") as f:
#     #     f.write(date, + time, + choose)
#     #     choose += 1


# Enter Your password...........
if x == password:
    print("Acess Garanted.")
    # your_bank()
else:
    print('Acess Denied.')

while True:
    print("Hey",name ,"What are you want to do,\n1.Check Balance.\n2.Widraw.\n3.Deposit.Press 0 to exit.")  
    choise = int(input("Please Enter Your Demand: "))
    # to exit this program 
    if choise == 0:
        break

    # to check your current bank balance 
    if choise == 1:
        Check_Bal()

    # to widraw your money
    elif choise == 2:
        Widraw_bal()

    elif choise == 3:
        Deposit()

    else:
        print("Please Enter Valid Number!.")

    