#!/usr/bin/env python3
"""
    Name: des_module_shared_key.py
    Author: 
    Created:
    Purpose: DES encryption
    DES is considered a weak encryption algorithm and is not recommended
    for secure applications. More modern encryption algorithms like AES
    should be used for security-critical applications.
    It uses a 56 bit key (8 bytes)
"""
# pip install pycryptodome
from Crypto.Cipher import DES
# Import hashlib for secure key derivation from shared key from user
import hashlib

# Get user input for the message and the shared key
plain_text = input("Enter message to encrypt: ")
shared_key = input("Enter shared key: ")


# Pad the key to 8 bytes using SHA-256 hash for compatibility with DES
# DES requires an 8-byte key, we derive one from the user-provided key

# Create a hash of the user-provided key using SHA-256
# Hash the user-provided key using SHA-256
hash_object = hashlib.sha256(shared_key.encode())

# Get the digest (the hashed value) as bytes
hashed_key_bytes = hash_object.digest()

# Assign the hashed key bytes to the 'hashed_key' variable
hashed_key = hashed_key_bytes

# Take the first 8 bytes of the hash to create a valid DES key
hashed_key = hashed_key[:8]


# Create a DES cipher object with the derived key
# in ECB (Electronic Codebook) mode
cipher = DES.new(hashed_key, DES.MODE_ECB)

# Convert (encode) message string to bytes
message_bytes = plain_text.encode()

# Ensure that the message length is a multiple of 8 bytes (required by DES)
while len(message_bytes) % 8 != 0:
    # Pad the message with spaces if needed to be a multiple of 8 bytes
    message_bytes += b' '

# Use the DES cipher to encrypt the padded message
encrypted_message = cipher.encrypt(message_bytes)

# Convert encrypted message to hexadecimal format
encrypted_message_hex = encrypted_message.hex()

# Print encrypted message in hexadecimal format
print(f"Encrypted message (in hexadecimal): {encrypted_message_hex}")

# Use the same DES cipher to decrypt the encrypted message
decrypted_message = cipher.decrypt(encrypted_message)

# Remove any trailing spaces from the decrypted message
decrypted_message_bytes = decrypted_message.rstrip(b' ')

# Decode the bytes to a string
decrypted_message = decrypted_message_bytes.decode()

# Print the decrypted message
print(f"Decrypted message: {decrypted_message} ")
