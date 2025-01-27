# Python3 code to implement Hill Cipher

keyMatrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
messageVector = [[0] for i in range(3)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

# Following function generates the
# key matrix for the key string
def getKeyMatrix(key):
	k = 0
	for i in range(3):
		for j in range(3):
			keyMatrix[i][j] = ord(key[k]) % 65
			k += 1

# Following function encrypts the message
def encrypt(messageVector):
	for i in range(3):
		for j in range(1):
			cipherMatrix[i][j] = 0
			for x in range(3):
				cipherMatrix[i][j] += (keyMatrix[i][x] *
									messageVector[x][j])
			cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):

	# Get key matrix from the key string
	getKeyMatrix(key)

	# Generate vector for the message
	for i in range(3):
		messageVector[i][0] = ord(message[i]) % 65

	# Following function generates
	# the encrypted vector
	encrypt(messageVector)

	# Generate the encrypted text 
	# from the encrypted vector
	CipherText = []
	for i in range(3):
		CipherText.append(chr(cipherMatrix[i][0] + 65))

	# Finally print the ciphertext
  return CipherText

# Driver Code
def generate_key():
  for letter in range(random.randint(1,26)):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = ''.join(random.sample(alphabet, letter))
    return key

def encrypt_text(text):
  key = generate_key
  cipher_text = HillCipher(text, key)
def main():



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
    file = 'playfair_mini.csv'
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

