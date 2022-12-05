'''
Donation Text-Based Website Project
By Tyler Varzeas
12/3/2022
'''

from time import sleep
from donations_pkg.homepage import show_homepage, donate, show_donations, format_currency
from donations_pkg.user import login, register

# Global (Application) variable definitions
database = {
    "admin": "password123",
}
donation_strings = []
donation_amounts = []
authorized_user = ""


# Main application loop
while True:
    '''
    This is the main loop for the application
    '''
    show_homepage(authorized_user)

    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f"Logged in as: {authorized_user}.")

    choose_option = input("What would you like to do?:  ")
    if choose_option == "1":
        username = input("Username: ").lower()
        password = input("Password: ")
        authorized_user = login(database, username, password)

    elif choose_option == "2":
        username = input("\nUsername: ").lower()
        password = input("Password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif choose_option == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_amt = donate(authorized_user)
            donation_strings.append(
                f"{authorized_user} donated {format_currency(donation_amt)}")
            donation_amounts.append(donation_amt)

    elif choose_option == "4":
        total = show_donations(donation_strings, donation_amounts)
        print(f"Total donations: {format_currency(total)}")

    elif choose_option == "5":
        print("\nLogging you out...")
        sleep(1)
        print("Goodbye! See you next time.")
        break
