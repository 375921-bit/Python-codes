# Password_Generator_2

import random

def generator(length=8):
    if length < 8:
        return "The password is too short"
    elif length > 32:
        return "The password is too long"

    chars = ["abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+="]
    return ''.join(random.choice(chars) for _ in range(length))

print("Generated Password:", generator())