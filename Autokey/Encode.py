# A Python program to illustrate
# Autokey Cipher Technique
import re

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def auto_encryption(msg, key):
    """Encrypts the message using Autokey Cipher."""
    new_key = key + msg
    new_key = new_key[:len(msg)]
    encrypt_msg = ""
    
    for i in range(len(msg)):
        first = ALPHABET.index(msg[i])
        second = ALPHABET.index(new_key[i])
        total = (first + second) % 26
        encrypt_msg += ALPHABET[total]
    
    return encrypt_msg

def auto_decryption(msg, key):
    """Decrypts the message using Autokey Cipher."""
    current_key = key
    decrypt_msg = ""
    
    for i in range(len(msg)):
        get1 = ALPHABET.index(msg[i])
        get2 = ALPHABET.index(current_key[i])
        total = (get1 - get2) % 26
        total = total + 26 if total < 0 else total
        decrypt_msg += ALPHABET[total]
        current_key += ALPHABET[total]
    
    return decrypt_msg

def main():
    msg = "HELLO"
    key = "N"
    
    if re.match(r'[-+]?\d*.?\d+', key):
        key = ALPHABET[int(key) % 26]
    
    encrypted = auto_encryption(msg, key)
    decrypted = auto_decryption(encrypted, key)
    
    print(f"Plaintext : {msg}")
    print(f"Encrypted : {encrypted}")
    print(f"Decrypted : {decrypted}")

if __name__ == "__main__":
    main()
