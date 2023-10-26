"""Imports the necessary modules from the PyCryptodome library.
Generates a random 24-byte key for 3DES encryption.
Creates a 3DES cipher object using the generated key and the Electronic Codebook (ECB) mode.
Defines a message to be encrypted (you can replace it with your own message).
Pads the message to make its length a multiple of 8 bytes, which is required for 3DES.
Encrypts the message using the 3DES cipher and prints the result.
Decrypts the encrypted message and prints the decrypted text."""
# Import necessary modules from the PyCryptodome library
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes

# Generate a random 24-byte key
key = get_random_bytes(24)

# Create a 3DES cipher object with the generated key in ECB mode
cipher = DES3.new(key, DES3.MODE_ECB)

# Message to be encrypted
message = input("Your message to encrypt: ")

"""In this example, the initial length of the message may not be 
a multiple of 8. The while loop will add spaces to the message until
its length becomes a multiple of 8.

Code Analysis
Inputs
   message (string): The message to be encrypted.
Flow
The code snippet initializes a while loop.
The condition of the while loop checks if the length of the message
is not a multiple of 8.
If the condition is true, a space character is added to the message.
Steps 2 and 3 are repeated until the length of the message becomes a multiple of 8.
Outputs
# Padding the message to be a multiple of 8 bytes (required for DES3)"""
while len(message) % 8 != 0:
    message += ' '

# Encrypt the message
encrypted_message = cipher.encrypt(message.encode())

# Decrypt the message
decipher = DES3.new(key, DES3.MODE_ECB)
decrypted_message = decipher.decrypt(encrypted_message).decode().rstrip()


# Print the encrypted message
print("Encrypted message:", encrypted_message)
# Print the decrypted message
print("Decrypted message:", decrypted_message)
