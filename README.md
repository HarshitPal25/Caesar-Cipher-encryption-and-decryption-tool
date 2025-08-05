# 🔐 Caesar Cipher CLI Tool

A simple **Python command-line tool** to encrypt and decrypt messages using the **Caesar Cipher algorithm**.  

---

## 📖 About
The **Caesar Cipher** is one of the oldest and simplest encryption techniques.  
It works by shifting each letter in the message by a fixed number of positions in the alphabet.  

- Supports **both encryption and decryption**  
- Preserves **uppercase and lowercase letters**  
- Keeps **numbers, spaces, and symbols unchanged**  

---

## 🚀 Features
- Encrypt any text with a custom shift value  
- Decrypt messages with the same shift value  
- Interactive **CLI menu** for easy usage  

---

## 🖥️ Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/caesar-cipher-cli.git
cd caesar-cipher-cli
```
```
python caesar_cipher.py
```

=== Caesar Cipher CLI Tool ===

Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter choice (1/2/3): 1

Enter message to encrypt: Hello World
Enter shift value: 3

🔒 Encrypted message: Khoor Zruog

Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter choice (1/2/3): 2

Enter message to decrypt: Khoor Zruog
Enter shift value: 3

🔓 Decrypted message: Hello World
