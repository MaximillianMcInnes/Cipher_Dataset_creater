# -*- coding: utf-8 -*-
from unicodedata import normalize
import re

def generate_array(key=''):
    """Create Polybius square with transposition."""
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I and J are combined
    array = []
    _tmp = []
    key = re.sub(r'[^a-zA-Z]+', '', key).upper()  # Remove non-alpha characters and uppercase

    if key:
        for k in key:
            alphabet = alphabet.replace(k, '')  # Remove characters in the key from the alphabet
        alphabet = key + alphabet

    for y in range(5):
        for x in range(5):
            _tmp.append(alphabet[0 + 5 * y + x])
        array.append(_tmp)
        _tmp = []

    return array

def display_array(array):
    """Display Polybius square."""
    print("Polybius Square:")
    print("      1   2   3   4   5")
    for row_label, row in zip(['1', '2', '3', '4', '5'], array):
        print(f" {row_label} [{ ' '.join('%03s' % i for i in row) }]")

def format_cipher(data):
    """Format cipher with spaces."""
    return " ".join(data[i:i + 2] for i in range(0, len(data), 2))

def encode(words, array):
    """Polybius square encryption."""
    cipher = ''
    words = normalize('NFKD', words).encode('ascii', 'ignore').decode()  # Replace accented characters
    for word in words.upper():
        for i in range(len(array)):
            if word in array[i]:
                oy = str(i + 1)
                ox = str(array[i].index(word) + 1)
                cipher += oy + ox
    return cipher

def decode(numbers, array):
    """Polybius square decryption."""
    numbers = re.sub(r'[^0-9]+', '', numbers)  # Remove non-digit characters
    text = ''
    for number in range(0, len(numbers), 2):
        try:
            oy = int(numbers[number]) - 1
            ox = int(numbers[number + 1]) - 1
            text += array[oy][ox]
        except IndexError:
            pass
    return text

def main():
    print("Polybius Square Encryption/Decryption")
    key = input("Enter a key for the Polybius square (optional): ").strip()
    array = generate_array(key)
    display_array(array)

    while True:
        mode = input("\nChoose mode: (e)ncrypt or (d)ecrypt or (q)uit: ").strip().lower()
        if mode == 'q':
            print("Exiting. Goodbye!")
            break
        elif mode in ['e', 'd']:
            text = input("Enter the text: ").strip()
            if mode == 'e':
                result = format_cipher(encode(text, array))
                print(f"Encrypted: {result}")
            elif mode == 'd':
                result = decode(text, array)
                print(f"Decrypted: {result}")
        else:
            print("Invalid choice. Please select 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
