from math import ceil

def encrypt(message, rod):
    # Pad the message to make its length divisible by the rod size
    padding_length = (rod - len(message) % rod) % rod
    message += " " * padding_length

    # Create a 2D grid for encryption
    grid = [[] for _ in range(rod)]
    for i, char in enumerate(message):
        grid[i % rod].append(char)

    # Flatten the grid to produce the encrypted message
    encrypted_message = "".join("".join(row) for row in grid)
    print(f"Encrypted message: {encrypted_message}")
    return encrypted_message

def decrypt(encrypted_message, rod):
    # Determine the number of columns
    num_cols = ceil(len(encrypted_message) / rod)

    # Reconstruct the 2D grid for decryption
    grid = [[] for _ in range(rod)]
    index = 0
    for row in range(rod):
        for col in range(num_cols):
            if index < len(encrypted_message):
                grid[row].append(encrypted_message[index])
                index += 1

    # Read the decrypted message row by row
    decrypted_message = "".join(grid[row][col] for col in range(num_cols) for row in range(rod) if col < len(grid[row]))
    print(f"Decrypted message: {decrypted_message.strip()}")
    return decrypted_message.strip()

def encrypt_text(text):
  text = text.strip()
  rod = random.randint(2,(len(text) // 5))
  return encrypt(text, rod)

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
            for cipher_text, key in encrypt_text(part):
                save_to_csv(cipher_text, key)


if __name__ == "__main__":
    main()


