import re

# the menu
def menu():
    menu_input = int(input("press 1 to login and 2 to stay in menu\n"))
    if menu_input == 1:
        login()
    if menu_input == 2:
        menu()
    else:
        print("request cannot be processed")

# the right password
def login():
    valid_email = (r'\b[\w|.|-]+@[\w|.|-]+[\w{2-4}]$')
    valid_password = '((?=.*\d+)(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\W+).{8,})'
    email = input("enter your email: ")
    email_match = re.match(valid_email, email)
    if email_match:
        print("email valid")
    password = input("enter your password: ")
    password_match = re.match(valid_password, password)
    if password_match:
        print("password valid")
        print("going back to menu")
    menu()

    if not email_match and not password_match:
        invalid()

def invalid():
    while True:
        valid_email = (r'\b[\w|.|-]+@[\w|.|-]+[\w{2-4}]$')
        valid_password = '((?=.*\d+)(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\W+).{8,})'
        email = input("enter your email: ")
        email_match = re.match(valid_email, email)
        password = input("enter your password: ")
        password_match = re.match(valid_password, password)
        email_count = 0
        password_count = 0
        if email_count < 3:
            email_count += 1
            if not email_match :
                print("invalid email")
                menu()
                break
        elif password_count < 3:
            password_count += 1
            if not password_match:
                print("invalid password")
                menu()
                break




# the first that wi;ll display
start = int(input("hello welcome \npress 1 to login and press 2 to exit \nEnter: "))
if start == 1:
    login()

elif start == 2:
    exit(0)