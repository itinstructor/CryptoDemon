#!/usr/bin/env python3
"""
    Name: des_module_generated_key.py
    Author: 
    Created:
    Purpose: DES encryption
"""
# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


def main():
    """Test DES encryption module"""
    plain_text = input("Text to encrypt: ")
    des_encrypt(plain_text)


def des_encrypt(plain_text):
    """Encrypt plain text with DES"""
    # Create a DES key (must be 8 bytes)
    key = get_random_bytes(8)
    # Create a DES cipher object using the key
    # and the Electronic Codebook (ECB) mode.
    cipher = DES.new(key, DES.MODE_ECB)

    # Data to encrypt
    data = bytes(plain_text, "utf-8")

    # Padding the data to be a multiple of 8 bytes (DES block size)
    padding_length = 8 - (len(data) % 8)
    data += bytes([padding_length]) * padding_length

    # Encrypt the data using the DES cipher
    encrypted_data = cipher.encrypt(data)

    # Decrypt the data using the DES cipher
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove the padding from the decrypted data
    padding_length = decrypted_data[-1]
    decrypted_data = decrypted_data[:-padding_length]

    # Convert decrypted bytes to string
    original_text = decrypted_data.decode('utf-8')

    # Print results
    print(f"  Original Text: {plain_text}")
    print(f"     Shared Key: {key.hex()}")
    print(f" Encrypted Data: {encrypted_data}")
    print(f" Decrypted Text: {original_text}")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
