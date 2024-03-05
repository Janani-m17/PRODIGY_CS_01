---

# Caesar Cipher Encryption and Decryption Program

This Python program implements a simple encryption and decryption system based on the Caesar cipher algorithm. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features

- Encrypt text with a specified shift value.
- Decrypt text using the same shift value.
- Option to choose between encryption and decryption.
- Option to exit the program after each operation.

## How to Use

1. Run the `main.py` script.
2. Enter the text you want to encrypt or decrypt when prompted.
3. Enter the value by which you want to shift the characters (positive for encryption, negative for decryption).
4. Choose the operation (encrypt or decrypt) by typing either "encrypt" or "decrypt" when prompted.
5. View the encrypted or decrypted text.
6. Decide whether to exit the program or perform another operation.

## How it works

```bash
python main.py
```

```plaintext
Enter the Text: Hello, World!
Enter the value to shift: 3
Choose operation (encrypt/decrypt): encrypt
Encryption:  Khoor, Zruog!
Do you want to exit? (yes/no): no
Enter the Text: Khoor, Zruog!
Enter the value to shift: 3
Choose operation (encrypt/decrypt): decrypt
Decryption:  Hello, World!
Do you want to exit? (yes/no): yes
```

## Learning

Through this project, I learned:

1. **Security-aware Programming:** Understanding the importance of safely handling data to prevent security issues.

2. **Encryption Basics:** Learning how basic encryption methods can protect sensitive information.

3. **Input Validation:** Making sure user input is safe to use to prevent security vulnerabilities.

4. **Code Organization:** Seeing the benefits of organizing code neatly for readability and security.

5. **Cryptographic Concepts:** Getting an introduction to encryption principles like the Caesar cipher.

---
