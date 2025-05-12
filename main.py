users = {
    "sithLord": "Ancient enimes r us",
    "d_Vader": "I'm Your Father",
    "GENERALleia": "May the Force be with you",
    "grogu": "patu",
    "there_is_no_try": "Yoda",
    "MyRey": "I Am All The Jedi",
    "Luke": "May the Force be with you"
}

def logged():
    print("Success!")
    while True:
        try:
            geek = int(input("1. Change password\n2. Log out\nChoose an option: "))
            if geek == 1:
                change = input("What would you like to change your password to? ")
                print(f"Your password '{change}' has been confirmed.")
                return
            elif geek == 2:
                print("Logged out.")
                return
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")

def login():
    username = input("Username? ")
    if username in users:
        password = input("Password? ")
        if users[username] == password:
            print("Logged in!")
            logged()
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

def register():
    username = input("Choose a username: ")
    if username in users:
        print("Username is already taken.")
    else:
        password = input("Choose a password: ")
        users[username] = password
        print("Registration successful!")
        logged()

def main():
    while True:
        try:
            menu = int(input("1. Login\n2. Register\n3. Quit\nChoose an option: "))
            if menu == 1:
                login()
            elif menu == 2:
                register()
            elif menu == 3:
                print("Terminated.")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
    