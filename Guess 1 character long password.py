import re

def strength(password)
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'[a-z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[^A-Za-z0-9]', password):
        score += 1
    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"

password1 = input("Password 1: ")
password2 = input("Password 2: ")

print("Password 1:", strength(password1))
print("Password 2:", strength(password2))