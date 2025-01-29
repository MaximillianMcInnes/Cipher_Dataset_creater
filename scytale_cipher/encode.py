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

def main():
    print("Scytale Cipher")
    choice = input("Choose an option (encrypt/decrypt): ").strip().lower()

    if choice == "encrypt":
        message = input("Enter the plaintext message: ").strip()
        rod = int(input("Enter the rod size: "))
        encrypt(message, rod)
    elif choice == "decrypt":
        encrypted_message = input("Enter the encrypted message: ").strip()
        rod = int(input("Enter the rod size: "))
        decrypt(encrypted_message, rod)
    else:
        print("Invalid option. Please choose 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
