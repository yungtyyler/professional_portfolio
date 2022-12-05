'''
Account Functions
By Tyler Varzeas
11/26/2022
'''


def show_balance(balance):
    '''
    Shows the current balance of the User's account
    '''
    print(f"Current Balance: {format_currency(balance)}")


def deposit(balance):
    '''
    Allows the User to deposit into their account
    '''
    amount = float(input("Enter Amount to be Deposited:   $"))
    updated_balance = float(balance + amount)
    return updated_balance


def withdraw(balance):
    '''
    Allows the User to withdraw from their account
    '''
    amount = float(input("Enter Amount to Withdraw:   $"))
    updated_balance = float(balance - amount)
    return updated_balance


def logout(name):
    '''
    Logs the user out of their account
    '''
    print(f"Goodbye {name}!")

# format currency


def format_currency(bal):
    '''
    format float to currency string
    '''
    return f"${bal:,.2f}"
