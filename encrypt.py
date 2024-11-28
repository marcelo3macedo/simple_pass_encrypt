import random
import getpass

def generate_encryption_key(password):
    """Generate a pseudo-random key based on the password."""
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
    """Encrypt the text using the provided key and add random characters for increased length."""
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
    
    print("\nEncrypted text:")
    print(encrypted_text)

if __name__ == "__main__":
    main()
