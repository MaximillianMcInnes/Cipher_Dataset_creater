import random
import string
from pycipher import ADFGVX

def encrypot_text(text):
  # Create ADFGVX cipher with the random key and keyword
  # Generate a random key using all alphanumeric characters
  characters = string.ascii_uppercase + string.digits  # A-Z and 0-9 (total 36 characters)
  random_key = ''.join(random.sample(characters, len(characters)))  # Random permutation

  # Generate a random keyword of a length between 1 and the maximum length - 1
  max_keyword_length = len(characters) - 1
  random_keyword_length = random.randint(1, max_keyword_length)
  random_keyword = ''.join(random.choices(string.ascii_uppercase, k=random_keyword_length))

  # Create ADFGVX cipher with the random key and keyword
  adfgvx = ADFGVX(key=random_key, keyword=random_keyword)

  # Example message
  text = "Hello world!"
  ciphertext = adfgvx.encipher(text)
  plaintext = adfgvx.decipher(ciphertext)

  # Output
  print(f"Random Key: {random_key}")
  print(f"Random Keyword: {random_keyword}")
  print(f"Ciphertext: {ciphertext}")
  print(f"Decrypted: {plaintext}")
  return ciphertext, random_key, random_keyword

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
