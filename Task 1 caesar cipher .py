letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:
        letter = letter.lower()
        if letter != " ":
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
        else:
            ciphertext += letter  # Keep spaces as is

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:
        letter = letter.lower()
        if letter != " ":
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
        else:
            plaintext += letter  # Keep spaces as is

    return plaintext


print()
print("*** Caesar Cipher python Project ***")
print()

print("Do you intend to encrypt or decrypt?")

user_input = input("encrypt/decrypt: ").lower()
print()

if user_input == "encrypt":
    print("encryption mode")
    print()
    key = int(input("Enter the key (1 and 10): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f'cipher: {ciphertext}')

elif user_input == "decrypt":
    print("decryption mode")
    print()
    key = int(input("Enter the key (1 and 10): "))
    text = input("Enter the text to decrypt: ")
    plaintext = decrypt(text, key)
    print(f'plaintext: {plaintext}')