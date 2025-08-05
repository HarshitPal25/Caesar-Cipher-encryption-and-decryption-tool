
def caesarcipher(text,shift):

    """Encrypts text using Caesar Cipher with given shift."""

    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result
def decryption(text,shift):

    """Decrypts text using Caesar Cipher with given shift."""

    return caesarcipher(text,-shift)
''' here you choose the given '''
def main():
    print("=== Caesar Cipher CLI Tool ===")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            message = input("Enter message to encrypt: ")
            shift = int(input("Enter shift value: "))
            encrypted = caesarcipher(message, shift)
            print(f"\n Encrypted message: {encrypted}")

        elif choice == "2":
            message = input("Enter message to decrypt: ")
            shift = int(input("Enter shift value: "))
            decrypted = decryption(message, shift)
            print(f"\n Decrypted message: {decrypted}")

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__" :
    main()