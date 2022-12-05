'''
Homepage functions
by Tyler Varzeas
12/3/2022
'''


def show_homepage(authorized_user):
    '''
    Homepage View Function
    name:string
    return:none
    '''

    print("")
    print("      === DonateMe Homepage ===         ")
    print("----------------------------------------")
    print("| 1.    Login     | 2.    Register     |")
    print("----------------------------------------")
    print("----------------------------------------")
    print("| 3.    Donate    | 4.  Show Donations |")
    print("----------------------------------------")


def donate(username):
    '''
    Donation function
    '''
    float_amount = None
    while True:
        '''
        This while loop will check if the user has input a valid number, and if they have converts it to a float.
        The try/except statement will check if the user has entered a valid amount.
        If the user has not entered a valid amount the loop will repeat.
        If the user has entered a valid amount, the loop will break and return the donation amount as a float.
        '''
        donation_amt = input("Enter amount to donate: ")
        try:
            float_amount = float(donation_amt)
        except ValueError:
            print("Please enter a valid amount.".format(input = donation_amt))
            continue

        if float_amount <= 0: 
            print("Donation cannot be zero or a negative number, try again!")
            continue   
        else:
            print(f"Thank you {username} for your donation!")
            break
    return float_amount

def show_donations(strings, numbers):
    '''
    This will display the donations made, and return a total amount to be displayed in the app.py module
    '''
    total = float(0)
    print("--- All Donations ---")
    if strings == []:
        print("There have been no donations :( ")
    for donation in strings:
        print(donation)
    for donation in numbers: 
        total += donation
    return total
        


def format_currency(bal):
    '''
    format float to currency string
    '''
    return f"${bal:,.2f}"