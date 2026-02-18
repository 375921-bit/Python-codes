def rsa_encrypt():
    key_input = input("Enter the encryption key (number): ")
    while not key_input.isdigit():
        print("Invalid input. Please enter a valid number.")
        key_input = input("Enter the encryption key (number): ")
        
rsa_encrypt()