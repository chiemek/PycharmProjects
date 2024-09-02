import re
#
#
# valid_email = (r'\b[\w|.|-]+@[\w|.|-]+[\w{2-4}]$')
# valid_password = '((?=.*\d+)(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\W+).{8,})'
#
# email = input("enter your email: ")
# email_match =re.match(valid_email,email)
#
# if email_match:
#     password = input("enter your password: ")
#     password_match = re.match(valid_password,password)
#
#     if password_match:
#         print("email and password valid")
#     else:
#         print("incorrect password")
# else:
#     print("incorrect email")


# assignment
import re
def menu():
    print("enter: \n1.Login \n2.Exit")


def validate_password():
    password = input("password: ")
    validpassword = re.match(password_pattern, password)
    return validpassword

def validate_email():
    email = input("email: ")
    validemail = re.match(email_pattern, email)
    return validemail

print("welcome to our program")
email_pattern = (r'\b[\w|.|-]+@[\w|.|-]+[\w{2-4}]$')
password_pattern = '((?=.*\d+)(?=.*[A-Z]+)(?=.*[a-z]+)(?=.*\W+).{8,})'

while True:
    email_count = 0
    password_count = 0

    menu()
    option = input(">>> ")
    if option == "1":
        while email_count < 3:
            email_count +=1

            if validate_email():
                print("valid email")

                while password_count < 3:
                    password_count += 1

                    if validate_password():
                        print("valid password")
                        print("login successful")
                        break

                    else:
                        print("invalid password")
                break
            else:
                print("invalid email")
    elif option == "2":
        exit(0)
    else:
        print("invalid input")

