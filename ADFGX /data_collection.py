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

def encode(message):
    # Prompt user for plaintext input.
    plaintext = input("Enter plaintext to encrypt: ").strip()
    
    # Encrypt the plaintext.
    ciphertext, key, keyword = encrypt_adfgx(message)
    
    # Display the encryption results.
    print("\nEncryption Results:")
    print("Randomly Generated Key (25 letters, omit 'J'):", key)
    print("Randomly Generated Keyword:", keyword)
    print("Ciphertext:", ciphertext)


def get_random_article_title():
    try:
        response = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=random&rnlimit=1&format=json")
        response.raise_for_status()
        data = response.json()
        title = data['query']['random'][0]['title']
        return title
    except requests.RequestException:
        print("Error fetching random article title.")
        return None


def get_wikipedia_article_text(article_title):
    user_agent = "MyWikipediaScript/1.0 (https://example.com)"
    wiki_wiki = wikipediaapi.Wikipedia(
        language='en',
        extract_format=wikipediaapi.ExtractFormat.WIKI,
        user_agent=user_agent
    )
    try:
        page = wiki_wiki.page(article_title)
        if not page.exists():
            print(f"Article '{article_title}' does not exist.")
            return None
        return page.text
    except Exception as e:
        print(f"Error fetching article '{article_title}': {e}")
        return None


def split_text_randomly(text, min_chars=1000, max_chars=3000):
    parts = []
    i = 0
    if len(text) < 500:
      skip = True
    if skip:
      while i < len(text):
          split_point = random.randint(min_chars, max_chars)
          parts.append(text[i:i + split_point])
          i += split_point
      return parts
    else:
      return text

def save_to_csv(cipher_text, key):
    print(cipher_text)
    file = 'polybuis_mini.csv'
    if nonsense(cipher_text):
        file_exists = Path(file).is_file()
        with open(file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["CipherText", "Key"])
            writer.writerow([cipher_text, key])
    else:
        print(f"This string is English and will be ignored.")

def main():
    while True:
      article_title = get_random_article_title()

      text = get_wikipedia_article_text(article_title)
      if nonsense(text):
        print("text is nonsense")
      else:

        if text is not None:
            parts = split_text_randomly(text, min_chars=1000, max_chars=3000)  # Adjusted for demonstration

        for part in parts:
            for cipher_text, key, keyword encrypt_text(part):
                save_to_csv(cipher_text, key)


if __name__ == '__main__':
    main()
