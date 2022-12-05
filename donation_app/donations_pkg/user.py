'''
User functions
By Tyler Varzeas
12/3/2022
'''


def login(database, username, password):
    '''
    login to the database
    '''
    if username in database and password == database[username]:
        print(f"\nWelcome back {username}!")
        return username
    elif username in database and password != database[username]:
        print("Incorrect password, try again.")
        return ""
    else:
        print("User not found, try again.")
        return ""


def register(database, username):
    '''
    Register to Database
    '''
    if username in database:
        print(f"\nUser {username} is already registered")
        return ""
    elif username not in database and len(username) >= 5 and len(username) < 10:
        print(f"\nUser {username} has been registered!")
        return username
    else:
        print(f"Username must be at least {5} characters and no more than {10} characters.")
        return ""