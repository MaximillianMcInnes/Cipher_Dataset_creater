
import re

# 默认密表
table = [['A', 'B', 'C', 'D', 'E'], 
         ['F', 'G', 'H', 'I', 'J'], 
         ['K', 'L', 'M', 'N', 'O'], 
         ['P', 'R', 'S', 'T', 'U'], 
         ['V', 'W', 'X', 'Y', 'Z']] 

# 
# 生成棋盘
# 
def generate_table(key = ''):
    # wiki原文：usually omitting "Q" or putting both "I" and "J" in the same location to reduce the alphabet to fit
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key = re.sub(r'[\W]', '', key).upper()

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key.replace(key[0], '')
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]
    return table

# 
# 加密
# 
def encrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L  = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += mangle(R, L, digraphs)
    return ciphertext


def mangle(R, L, digraphs):
    a = position(table, digraphs[0])
    b = position(table, digraphs[1])
    return R[a[0]][b[1]] + L[b[0]][a[1]]

# 
# 解密
# 
def decrypt(keys, words):
    ciphertext = ''
    words = re.sub(r'[\W]', '', words).upper().replace('Q', '')
    R, L = generate_table(key[0]), generate_table(key[1])

    for i in range(0, len(words), 2):
        digraphs = words[i:i+2]
        ciphertext += unmangle(R, L, digraphs)
    return ciphertext.lower()

def unmangle(R, L, digraphs):
    a = position(R, digraphs[0])
    b = position(L, digraphs[1])
    return table[a[0]][b[1]] + table[b[0]][a[1]]

# todo
def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return (row, col)
    return (None, None)
def generate_key():
  for letter in range(random.randint(1,26)):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''.join(random.sample(alphabet, letter))
    return key

def encrypt_text(text):
  key = [generate_key(), generate_key()]
  cipher_text = encrypt(key, text)
  return cipher_text
  
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
