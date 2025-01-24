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
    file = 'row_transposition.csv'
    if nonsense(cipher_text):
        file_exists = Path(file).is_file()
        with open(file, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["CipherText", "Key"])
            writer.writerow([cipher_text, key])

def cipher_encryption(msg , key):
    msg = msg.replace(" ", "").upper()
    # print(msg)
    key = key.upper()

    # assigning numbers to keywords
    kywrd_num_list = keyword_num_assign(key)

    # printing key
    for i in range(len(key)):
        print(key[i], end=" ", flush=True)
    # for
    print()
    for i in range(len(key)):
        print(str(kywrd_num_list[i]), end=" ", flush=True)
    # for
    print()
    print("-------------------------")

    # in case characters don't fit the entire grid perfectly.
    extra_letters = len(msg) % len(key)
    # print(extraLetters)
    dummy_characters = len(key) - extra_letters
    # print(dummyCharacters)

    if extra_letters != 0:
        for i in range(dummy_characters):
            msg += "."
    # if

    # print(msg)

    num_of_rows = int(len(msg) / len(key))

    # Converting message into a grid
    arr = [[0] * len(key) for i in range(num_of_rows)]
    z = 0
    for i in range(num_of_rows):
        for j in range(len(key)):
            arr[i][j] = msg[z]
            z += 1
        # for
    # for

    for i in range(num_of_rows):
        for j in range(len(key)):
            print(arr[i][j], end=" ", flush=True)
        print()
    # for

    # getting locations of numbers
    num_loc = get_number_location(key, kywrd_num_list)

    print(num_loc)

    # cipher
    cipher_text = ""
    k = 0
    for i in range(num_of_rows):
        if k == len(key):
            break
        else:
            d = int(num_loc[k])
        # if
        for j in range(num_of_rows):
            cipher_text += arr[j][d]
        # for
        k += 1
    # for

    print("Cipher Text: {}".format(cipher_text))


def get_number_location(key, kywrd_num_list):
    num_loc = ""
    for i in range(len(key) + 1):
        for j in range(len(key)):
            if kywrd_num_list[j] == i:
                num_loc += str(j)
            # if
        # for
    # for
    return num_loc


def keyword_num_assign(key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    kywrd_num_list = list(range(len(key)))
    # print(kywrdNumList)
    init = 0
    for i in range(len(alpha)):
        for j in range(len(key)):
            if alpha[i] == key[j]:
                init += 1
                kywrd_num_list[j] = init
            # if
        # inner for
    # for
    return kywrd_num_list

def generate_key():
  for letter in range(random.randint(1,26)):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''.join(random.sample(alphabet, letter))
    return key

def encypt(text):
  key = generate_key()
  cipher_text = cipher_encryption(text, key)
  return cipher_text, key

      article_title = get_random_article_title()

      text = get_wikipedia_article_text(article_title)
      if nonsense(text):
        print("text is nonsense")
      else:

       
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
            for cipher_text, key in encrypt_text(part):
                save_to_csv(cipher_text, key)

if __name__ == "__main__":
    main()
