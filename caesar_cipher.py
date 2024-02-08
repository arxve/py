def caesar_cipher_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase
            is_upper = char.isupper()
            # Apply the Caesar Cipher shift
            shifted_char = chr((ord(char) + shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return result

def caesar_cipher_decrypt(ciphertext, shift):
    # To decrypt, use the negative shift value
    return caesar_cipher_encrypt(ciphertext, -shift)

if __name__ == "__main__":
    # Input the text and shift value
    plaintext = input("Enter the text to encrypt: ")
    shift_value = int(input("Enter the shift value: "))

    # Encrypt the text
    ciphertext = caesar_cipher_encrypt(plaintext, shift_value)
    print(f"Encrypted text: {ciphertext}")

    # Decrypt the text
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift_value)
    print(f"Decrypted text: {decrypted_text}")
