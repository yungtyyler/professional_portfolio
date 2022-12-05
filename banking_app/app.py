'''
ATM Project
By Tyler Varzeas
11/26/2022
'''

from banking_pkg.account import show_balance, deposit, withdraw, logout, format_currency
from time import sleep

while True:
    name = input("Enter name to register:   ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
    elif name == None:
        print("You must enter a name.")
    else:
        break
    
while True:
    pin = input("Enter PIN:   ")
    if len(pin) > 4:
        print("PIN must contain 4 characters")
    else:
        break

balance = 0

print(f"{name} has registered with a starting balance of ${balance}\n")

def atm_menu(name):
    '''
    Main Menu Display
    name:string
    return:none
    '''

    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

while True:
    
    print("LOGIN")
    name_to_validate = input("Enter Name:   ")
    pin_to_validate = input("Enter PIN:   ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login Successful")
        break
    else:
        print("Invalid credentials")

while True:
    atm_menu(name)
    option = input("\nChoose an option:   ")

    if option == "1":
        show_balance(balance)
        sleep(2)
    
    elif option == "2":
        updated_balance = deposit(balance)
        balance = updated_balance
        print(f"Current Balance: {format_currency(balance)}")
        sleep(2)
    
    elif option == "3":
        updated_balance = withdraw(balance)
        if updated_balance > balance or updated_balance < 0:
            print("You don't have that much cash!")
        elif updated_balance < balance:
            balance = updated_balance
            print(f"Current Balance:   {format_currency(balance)}")
        sleep(2)

    elif option == "4":
        logout(name)
        sleep(2)
        break

    else:
        print("Invalid option, try again")