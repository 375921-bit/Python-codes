def encode(text, shift):
    # Shift characters and convert to binary
    shifted = ''.join(chr((ord(c) + shift) % 256) for c in text)
    return ' '.join(format(ord(c), '08b') for c in shifted)

def decode(binary, shift):
    # Convert binary to shifted text
    shifted_text = ''.join(chr(int(b, 2)) for b in binary.split())
    # Reverse shift
    original = ''.join(chr((ord(c) - shift) % 256) for c in shifted_text)
    return original

# Ask user for the key (shift amount)
while True:
    try:
        key = int(input("\nEnter your private key (number 0-255): "))
        break
    except:
        print("Please enter a valid number.")

while True:
    choice = input("\nWould you like to encode, decode, or exit: ").lower()

    if choice == 'encode':
        message = input("Enter message: ")
        print("Encrypted binary:", encode(message, key))
    elif choice == 'decode':
        binary_message = input("Enter binary: ")
        try:
            print("Decrypted message:", decode(binary_message, key))
        except:
            print("Invalid binary input.")
    elif choice == 'exit':
        break
    else:
        print("Invalid option.")