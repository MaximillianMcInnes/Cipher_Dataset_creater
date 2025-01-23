import string
import random
import wikipediaapi
import requests
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








# Python3 implementation of
# Columnar Transposition
import math




def encryptMessage(msg, key):
    cipher = ""

    # track key indices
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))

    # add the padding character '_' in empty
    # the empty cell of the matix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    # create Matrix and insert message and
    # padding characters row-wise
    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1

    return cipher

def encrypt(text):
  key = generate_key()
  cipher_text = encryptMessage(msg, key)
  return cipher_text, key

# This code is contributed by Aditya K


def save_to_csv(text, key):
  file = 'coolumare_transpostion.csv'
def generate_key():
  for letter in range(26):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''.join(random.sample(alphabet, letter))
    return key


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
            for ciphertext, key in format_cipher(encrypt(text))
                save_to_csv(ciphertext, key)

  #ok in this subroutine we get the text usally yap
  #then we get a random key and then encrypt it


if __name__ == '__main__':
  main()
