#!/usr/bin/env python3
"""
    Name: des_class.py
    Author: 
    Created: 09/29/2023
    Purpose: DES encryption demonstration using user input shared key
    3DES is considered a weak encryption algorithm and is not recommended
    for secure applications. More modern encryption algorithms like AES
    should be used for security-critical applications.
    It uses a 192 bit (24 bytes) key.
    Like DES, it uses an 8 byte block cipher.
    Data is encrypted 8 bytes at a time
    Data is padded to increments of 8 bytes.
"""
# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Import hashlib for secure key derivation from user shared key
import hashlib


class DESClass:
    def __init__(self, plain_text: str, shared_key: str = "") -> None:
        self.plain_text = plain_text
        self.shared_key = shared_key

    # ------------------------- ENCRYPT DES -------------------------------#
    def encrypt(self):
        """Encrypt plain text with DES"""
        if self.shared_key == "":
            # If the user does not enter a shared key
            # Create a random DES key (must be 8 bytes)
            # from pycryptodome library
            self.key = get_random_bytes(8)

            # Create a DES cipher object using the key
            # and the Electronic Codebook (ECB) mode.
            self.cipher = DES.new(self.key, DES.MODE_ECB)

        else:
            # If the user enters a shared key
            # DES requires an 8-byte key,
            # Pad user entered shared key to 8 bytes
            # Use SHA-256 hash to derive a 8-byte key
            # from the user-provided key

            # Create a hash of the user-provided key using SHA-256
            hashed_key = hashlib.sha256(self.shared_key.encode())
            hashed_key_bytes = hashed_key.digest()

            # Slice the first 8 bytes of the hash to
            # create a valid 8-byte DES key
            self.key = hashed_key_bytes[:8]

            # Create a DES cipher object with the derived key
            # in ECB (Electronic Codebook) mode
            self.cipher = DES.new(self.key, DES.MODE_ECB)

        # Convert (encode) message string to bytes
        message_bytes = self.plain_text.encode()

        # Ensure that the message length is a multiple
        # of 8 bytes (required by DES)
        # Pad the end of the message if needed
        while len(message_bytes) % 8 != 0:
            # Pad the end of the message with spaces if needed
            message_bytes += b" "

        # Use the DES cipher object to encrypt the padded message
        self.encrypted_data = self.cipher.encrypt(message_bytes)

    # ------------------------- DECRYPT DES -------------------------------#
    def decrypt(self):
        """Decrypt DES encrypted data to plain text"""
        # Use the same DES cipher object to decrypt the encrypted message
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
    des = DESClass(plain_text, shared_key)

    des.encrypt()
    des.decrypt()

    # Print results
    print(f"  Original Text: {des.plain_text}")
    print(f"     Shared Key: {des.key.hex()}")
    print(f" Encrypted Data: {des.encrypted_data.hex()}")
    print(f" Decrypted Text: {des.decrypted_data} ")


# If a standalone program, call the main function
# Else, use as a module
if __name__ == "__main__":
    main()
