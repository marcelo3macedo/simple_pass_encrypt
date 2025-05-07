import random
import getpass
import pyperclip

def generate_encryption_key(password):
    random.seed(password)
    characters = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "abcdefghijklmnopqrstuvwxyz"
        "0123456789"
        "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    )
    shuffled = list(characters)
    random.shuffle(shuffled)
    return dict(zip(characters, shuffled))

def encrypt_text(text, key, password):
    random.seed(password)
    encrypted = []
    characters_pool = list(key.values())
    for char in text:
        encrypted_char = key.get(char, char)
        random_addition = ''.join(random.choices(characters_pool, k=random.randint(1, 3)))
        encrypted.append(encrypted_char + random_addition)
    return ''.join(encrypted)

def main():
    password = getpass.getpass("Enter your password: ")
    text = input("Enter the text to encrypt: ")
    
    key = generate_encryption_key(password)
    encrypted_text = encrypt_text(text, key, password)
    
    pyperclip.copy(encrypted_text)
    print("\n✅ Encrypted text copied to clipboard. Just press Ctrl+V to paste.")

if __name__ == "__main__":
    main()
