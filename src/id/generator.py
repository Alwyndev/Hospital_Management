from random import choice as random_choice

SEED = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890!@#$%^&*"


def random_id(length=8):
    buffer = ""
    for i in range(length):
        buffer += random_choice(SEED)
    return buffer


print(random_id())
