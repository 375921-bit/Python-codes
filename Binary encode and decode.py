def encode(text):
    return ' '.join(format(ord(c), '08b') for c in text)

def decode(binary):
    return ''.join(chr(int(b, 2)) for b in binary.split())

while True:
    choice = input("Would you like to encode, decode, or exit? ").lower()

    if choice == 'encode':
        message = input("Enter message: ")
        print("Binary:", encode(message),"\n")
    elif choice == 'decode':
        binary_message = input("Enter binary: ")
        try:
            print("Decoded message:", decode(binary_message),"\n")
        except:
            print("Invalid binary input.")
    elif choice == 'exit':
        break
    else:
        print("Invalid option.")