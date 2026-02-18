print("Let's check your security. Answer y or n to each of the questions.")

phish = input("Can you recognize phishing emails? ").lower()
pw = input("Is your password strong? ").lower()
auth = input("Do you use multi-factor authentication? ").lower()
enc = input("Do you know how to encrypt sensitive information? ").lower()

if (phish == 'n' or pw == 'n' or auth == 'n' or enc == 'n'):
    print("You can improve your security habits.")
else:
    print("You have good security habits.")