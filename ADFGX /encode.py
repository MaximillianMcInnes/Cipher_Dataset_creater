#!/usr/bin/env python3
"""
ADFGX Cipher Encryption with Randomly Generated Key and Keyword

This script randomly generates:
  - A 25-letter key (from A–Z, omitting 'J') for the Polybius square.
  - A 6-letter keyword for the columnar transposition.
Then, it encrypts the provided plaintext using the ADFGX cipher.
Requires the pycipher package.
"""

import random
import string
from pycipher.polybius import PolybiusSquare
from pycipher.columnartransposition import ColTrans

def generate_random_key():
    """
    Generate a random 25-letter key (using A–Z excluding 'J').

    Returns:
        str: A string of 25 unique letters.
    """
    letters = [letter for letter in string.ascii_uppercase if letter != 'J']
    random.shuffle(letters)
    return ''.join(letters)

def generate_random_keyword(length=6):
    """
    Generate a random keyword of the specified length.

    Parameters:
        length (int): The length of the keyword (default is 6).

    Returns:
        str: A random keyword.
    """
    return ''.join(random.sample(string.ascii_uppercase, length))

def encrypt_adfgx(plaintext):
    """
    Encrypt the provided plaintext using the ADFGX cipher with a randomly generated key and keyword.

    Parameters:
        plaintext (str): The message to encrypt.

    Returns:
        tuple: A tuple containing (ciphertext, key, keyword).
            - ciphertext: The encrypted message.
            - key: The 25-letter key used for the Polybius square.
            - keyword: The keyword used for the columnar transposition.
    """
    # Randomly generate key and keyword
    key = generate_random_key()
    keyword = generate_random_keyword()

    # Step 1: Polybius Square encryption with the characters 'A', 'D', 'F', 'G', 'X'
    polybius_text = PolybiusSquare(list(key), size=5, chars='ADFGX').encipher(plaintext)

    # Step 2: Columnar Transposition encryption using the generated keyword
    ciphertext = ColTrans(keyword).encipher(polybius_text)
    
    return ciphertext, key, keyword

def main():
    # Prompt user for plaintext input.
    plaintext = input("Enter plaintext to encrypt: ").strip()
    
    # Encrypt the plaintext.
    ciphertext, key, keyword = encrypt_adfgx(plaintext)
    
    # Display the encryption results.
    print("\nEncryption Results:")
    print("Randomly Generated Key (25 letters, omit 'J'):", key)
    print("Randomly Generated Keyword:", keyword)
    print("Ciphertext:", ciphertext)

if __name__ == '__main__':
    main()
