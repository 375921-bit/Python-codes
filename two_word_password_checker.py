'''
import time

#Get information from the list
with open('two_word_password_checker.txt', 'r') as file:
    known_passwords = [line.strip() for line in file]

#Get user password
password = input("Enter a password: ")

#Check the user's password amd give feedback
def test_password(password, known_passwords):
    start_time = time.time()
    
    if password in known_passwords:
        print("Your password has been detected.")
    else:
        print("Password not detected.")
    
    end_time = time.time()  # Record end time
    duration = end_time - start_time
    print("Test completed in",duration,"seconds.")

test_password(password, known_passwords)
'''