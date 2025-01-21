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


def encryptRailFence(s,n):
      fence = [[] for i in range(n)]
      rail  = 0
      var   = 1

      for char in s:
        fence[rail].append(char)
        rail += var

        if rail == n-1 or rail == 0:
          var = -var

      res = ''
      for i in fence:
        for j in i:
          res += j

      return res


def encrypt_text(text):
    for key in range(2, 99):
        encrypted_text = encryptRailFence(text, key)
        yield encrypted_text, key


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
