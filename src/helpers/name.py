def is_valid_name(name):
    is_valid = True
    for letter in name:
        if not (letter.isalpha() or letter.isspace()):
            is_valid = False
    return is_valid


def get_name():
    while True:
        name = input("Enter your name please: ")
        if is_valid_name(name):
            return name
        else:
            print("That name isn't valid, names only contains letters and spaces, let's try that again...")
