# -*- coding: utf-8 -*-
from unicodedata import normalize
import re
import numpy
import string
import requests
import wikipediaapi
import random
import csv
from pathlib import Path
import pandas as pd
from nostril import nonsense


def save_to_csv(cipher_text, key):
    print(cipher_text)
    file = 'railfencemini.csv'
    if nonsense(cipher_text):
        file_exists = Path(file).is_file()
        with open(file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["CipherText", "Key"])
            writer.writerow([cipher_text, key])
    else:
        print(f"This string is English and will be ignored.")

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

def create_key():
  alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # I and J are combined
  for letter in range(len(alphabet)):
    key = ''.join(random.sample(alphabet, len(alphabet)))
  return key

def main():
    while True:
      article_title = get_random_article_title()
      text = get_wikipedia_article_text(article_title)
      if nonsense(text):
        print("text is nonsense")
      else:
        key = create_key()
        array = generate_array(key)
        display_array(array)
        if text is not None:
            parts = split_text_randomly(text, min_chars=1000, max_chars=3000)  # Adjusted for demonstration

        for part in parts:
            for ciphertext in format_cipher(encode(text, array))
                save_to_csv(cipher_text, key)




if __name__ == "__main__":
    main()








def main():

