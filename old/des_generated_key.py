#!/usr/bin/env python3
"""
    Name: des_generated_key.py
    Author: 
    Created: 09/29/2023
    Purpose: DES encryption demonstration using random key
    DES is considered a weak encryption algorithm and is not recommended
    for secure applications. More modern encryption algorithms like AES
    should be used for security-critical applications.
    It uses a 56 bit key. The initial key consists of 64 bits (8 bytes).
    Before the DES process even starts, every 8th bit of the key is
    discarded to produce a 56-bit key. 
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

    # Convert (encode) message string to bytes
    message_bytes = plain_text.encode()

    # Ensure that the message length is a multiple of 8 bytes (required by DES)
    while len(message_bytes) % 8 != 0:
        # Pad the message with spaces if needed to be a multiple of 8 bytes
        message_bytes += b' '

    # Encrypt the data using the DES cipher
    encrypted_data = cipher.encrypt(message_bytes)

    # Decrypt the data using the DES cipher
    decrypted_data = cipher.decrypt(encrypted_data)

    # Remove any trailing spaces from the decrypted message
    decrypted_data_bytes = decrypted_data.rstrip(b' ')

    # Convert decrypted bytes to string
    decrypted_data = decrypted_data_bytes.decode('utf-8')

    # Print results
    print(f"  Original Text: {plain_text}")
    print(f"     Shared Key: {key.hex()}")
    print(f" Encrypted Data: {encrypted_data.hex()}")
    print(f" Decrypted Text: {decrypted_data}")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
