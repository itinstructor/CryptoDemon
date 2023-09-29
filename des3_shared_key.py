#!/usr/bin/env python3
"""
    Name: des3_shared_key.py
    Author: 
    Created: 09/29/2023
    Purpose: 3DES encryption demonstration using user input shared key
    3DES is considered a weak encryption algorithm and is not recommended
    for secure applications. More modern encryption algorithms like AES
    should be used for security-critical applications.
    It uses a 192 bit (24 bytes) key.
    Like DES, it uses an 8 byte block cipher.
    Data is encrypted 8 bytes at a time
    Data must be padded to increments of 8 bytes.
"""
# pip install pycryptodome
from Crypto.Cipher import DES3
# Import hashlib for secure key derivation from shared key from user
import hashlib


def main():
    """Test DES encryption module"""
    # Get user input for the message and the shared key
    plain_text = input("Text to encrypt: ")
    shared_key = input("Shared key: ")
    des_encrypt(plain_text, shared_key)


def des_encrypt(plain_text, shared_key):
    """Encrypt plain text with DES"""
    # Pad the key to 24 bytes using SHA-256 hash for compatibility with 3DES
    # Triple DES (3DES)  requires an 24-byte key,
    # we derive one from the user-provided key

    # Create a hash of the user-provided key using SHA-256
    # Hash the user-provided key using SHA-256
    hashed_key = hashlib.sha256(shared_key.encode())
    hashed_key_bytes = hashed_key.digest()
    # Take the first 24 bytes of the hash to create a valid 24-byte 3DES key
    hashed_key_bytes = hashed_key_bytes[:24]

    # Create a DES cipher object with the derived key
    # in ECB (Electronic Codebook) mode
    cipher = DES3.new(hashed_key_bytes, DES3.MODE_ECB)

    # Convert (encode) message string to bytes
    message_bytes = plain_text.encode()
    # Ensure that the message length is a multiple of 8 bytes (required by DES)
    while len(message_bytes) % 8 != 0:
        message_bytes += b' '  # Pad the message with spaces if needed

    # Use the DES cipher to encrypt the padded message
    encrypted_data = cipher.encrypt(message_bytes)

    # Use the same DES cipher to decrypt the encrypted message
    decrypted_data_bytes = cipher.decrypt(encrypted_data)

    # Remove any trailing spaces from the decrypted message
    decrypted_data_bytes = decrypted_data_bytes.rstrip(b' ')

    # Decode the bytes to a string
    decrypted_data = decrypted_data_bytes.decode('utf-8')

    # Print results
    print(f"  Original Text: {plain_text}")
    print(f"     Shared Key: {hashed_key_bytes.hex()}")
    print(f" Encrypted Data: {encrypted_data.hex()}")
    print(f" Decrypted Text: {decrypted_data} ")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
