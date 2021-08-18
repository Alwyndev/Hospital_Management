import mysql.connector as sql


def get_password():
    while True:
        try:
            password = input("Create password: ")
            retyped_password = input("Retype password: ")
            if password != retyped_password:
                raise ValueError
            else:
                return password
        except ValueError:
            print("Passwords don't match, try again.")


def init_admin():
    admin_name = input("Enter admin name: ")
    admin_password = get_password()


