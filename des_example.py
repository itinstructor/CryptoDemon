# pip install pycryptodome
# Import necessary modules from PyCryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Generate a random 8-byte key
key = get_random_bytes(8)

# Create a DES cipher object with the generated key in ECB mode
cipher = DES.new(key, DES.MODE_ECB)

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
    message += " "

# Encrypt the message using the DES cipher
encrypted_message = cipher.encrypt(message.encode())

# Decrypt the message using the same key
decrypted_message = cipher.decrypt(encrypted_message).decode().strip()

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted_message}")
print("Decrypted Message:", decrypted_message)
