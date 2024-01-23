#!/usr/bin/env python3
"""
    Name: aes256_class.py
    Author: 
    Created: 09/29/2023
    Purpose: 3DES encryption demonstration using user input shared key
    It uses a 256 bit (24 bytes) key.
    It uses an 16 byte block cipher.
    Data is encrypted 16 bytes at a time
    Data is padded to increments of 16 bytes.
"""
# pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Import hashlib for secure key derivation from user shared key
import hashlib


class AESClass:
    def __init__(self, plain_text: str, shared_key: str = "") -> None:
        self.plain_text = plain_text
        self.shared_key = shared_key

    # ----------------- DECRYPT -------------------------------------------#
    def encrypt(self):
        """Encrypt plain text with 3DES"""
        if self.shared_key == "":
            # If the user does not enter a shared key
            # Create a random AES256 key (must be 32 bytes)
            # from pycryptodome library
            self.key = get_random_bytes(32)
            # Create a DES cipher object using the key
            # and the Electronic Codebook (ECB) mode.
            self.cipher = AES.new(self.key, AES.MODE_ECB)

        else:
            # If the user enters a shared key
            # AES256 requires an 32-byte key,
            # Pad user entered shared key to 32 bytes
            # Use SHA-256 hash to derive a 32-byte key
            # from the user-provided key

            # Create a hash of the user-provided key using SHA-256
            hashed_key = hashlib.sha256(self.shared_key.encode())
            hashed_key_bytes = hashed_key.digest()

            # Slice the first 32 bytes of the hash to
            # create a valid 232-byte AES256 key
            self.key = hashed_key_bytes[:32]

            # Create a DES cipher object with the derived key
            # in ECB (Electronic Codebook) mode
            self.cipher = AES.new(self.key, AES.MODE_ECB)

        # Convert (encode) message string to bytes
        message_bytes = self.plain_text.encode()

        # Ensure that the message length is a multiple
        # of 16 bytes (required by AES)
        # Pad the end of the message if needed
        while len(message_bytes) % 16 != 0:
            # Pad the end of the message with spaces if needed
            message_bytes += b" "

        # Use the AES cipher object to encrypt the padded message
        self.encrypted_data = self.cipher.encrypt(message_bytes)

    # ----------------- DECRYPT -------------------------------------------#
    def decrypt(self):
        """Decrypt AES encrypted data to plain text"""
        # Use the same AES cipher object to decrypt the encrypted message
        decrypted_data_bytes = self.cipher.decrypt(self.encrypted_data)

        # Remove any trailing spaces (padding) from the decrypted message
        decrypted_data_bytes = decrypted_data_bytes.rstrip(b" ")

        # Decode bytes to string
        self.decrypted_data = decrypted_data_bytes.decode("utf-8")


def main():
    """Test DES encryption module"""
    # Get user input for the message and the shared key
    plain_text = input("Text to encrypt: ")
    shared_key = input("Shared key: ")
    # Create object with plain text and shared key input arguments
    aes = AESClass(plain_text, shared_key)

    aes.encrypt()
    aes.decrypt()

    # Print results
    print(f"  Original Text: {aes.plain_text}")
    print(f"     Shared Key: {aes.key.hex()}")
    print(f" Encrypted Data: {aes.encrypted_data.hex()}")
    print(f" Decrypted Text: {aes.decrypted_data} ")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
