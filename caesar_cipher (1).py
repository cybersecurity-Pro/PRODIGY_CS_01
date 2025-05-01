
def caesar_cipher(text, shift, mode):
    result = ''
    shift = shift % 26  # Make sure the shift stays within alphabet bounds

    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        elif char.isdigit():
            shifted_char = str((int(char) + shift) % 10)
        else:
            shifted_char = char  # Leave symbols unchanged
        result += shifted_char
    return result

def main():
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            text = input("Enter the text to encrypt: ")
            try:
                shift = int(input("Enter the shift value: "))
                encrypted = caesar_cipher(text, shift, 'encrypt')
                print("Encrypted Text:", encrypted)
            except ValueError:
                print("Shift must be an integer.")
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            try:
                shift = int(input("Enter the shift value: "))
                decrypted = caesar_cipher(text, shift, 'decrypt')
                print("Decrypted Text:", decrypted)
            except ValueError:
                print("Shift must be an integer.")
        elif choice == '3':
            print("Exiting Caesar Cipher Program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
