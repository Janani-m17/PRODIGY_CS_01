def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

while True:
    text = input("Enter the Text: ")
    shift = int(input("Enter the value to shift: "))
    operation = input("Choose operation (encrypt/decrypt): ")

    if operation.lower() == 'encrypt':
        encrypted = caesar_cipher(text, shift, 'encrypt')
        print("Encryption: ", encrypted)
    elif operation.lower() == 'decrypt':
        decrypted = caesar_cipher(text, shift, 'decrypt')
        print("Decryption: ", decrypted)
    else:
        print("Invalid operation. Please choose encrypt or decrypt.")
        continue

    exit_choice = input("Do you want to exit? (yes/no): ")
    if exit_choice.lower() == 'yes':
        break
