# Text Encryption Program

A Python program that encrypts text using a user-provided password. The encrypted text includes uppercase and lowercase letters, numbers, and special characters, making it highly secure. The password input is masked for privacy.

## Features

- **Secure Password Input**: The password is entered without displaying characters on the screen.
- **Custom Encryption**: The password is used as a seed to generate a unique encryption key.
- **Special Characters Support**: Includes a mix of special characters, letters, and numbers in the encryption process.
- **Increased Text Length**: Appends random characters to the encrypted text for added complexity.

## How It Works

1. The user inputs a password (masked as `*`) and text to encrypt.
2. The program generates a pseudo-random encryption key based on the password.
3. Each character in the input text is mapped to an encrypted character.
4. Additional random characters are appended to the encrypted result for enhanced security.

## Requirements

- Python 3.x
- `getpass` (built-in Python module)

## Installation

1. Clone this repository or download the script.
2. Ensure Python 3.x is installed on your system.

## Usage

1. Run the program:
   ```bash
   python encrypt_text.py
