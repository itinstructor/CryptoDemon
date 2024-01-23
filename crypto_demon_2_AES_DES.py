# Import necessary libraries
# Tkinter for creating the graphical user interface
import tkinter as tk

# pip install cryptography
# Fernet for key generation
from cryptography.fernet import Fernet  

# Padding for message length
from cryptography.hazmat.primitives import padding

# Cipher for encryption/decryption
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Poly1305 for ChaCha20Poly1305
from cryptography.hazmat.primitives.poly1305 import Poly1305

# Serialization for key serialization
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # Key derivation
from cryptography.hazmat.primitives.asymmetric import dh, ec  # Asymmetric key exchange

# Backend for cryptographic operations
from cryptography.hazmat.backends import default_backend
import os  # Operating system interface for randomness

# Create a class for the encryption application


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption App")  # Set the window title

        # Create and place widgets using grid layout
        # Label for displaying the shared key
        self.shared_key_label = tk.Label(root, text="Shared Key:")
        self.shared_key_label.grid(
            row=0, column=0, columnspan=2
        )  # Grid layout position

        # Text input field for plain text
        self.plain_text_input = tk.Entry(root, width=40)
        self.plain_text_input.grid(
            row=1, column=0, columnspan=2
        )  # Grid layout position

        # Label for displaying encrypted text
        self.encrypted_text_label = tk.Label(root, text="Encrypted Text:")
        self.encrypted_text_label.grid(
            row=2, column=0, columnspan=2
        )  # Grid layout position

        # Label for displaying decrypted text
        self.decrypted_text_label = tk.Label(root, text="Decrypted Text:")
        self.decrypted_text_label.grid(
            row=4, column=0, columnspan=2
        )  # Grid layout position

        self.generate_key_button = tk.Button(
            root, text="Generate Shared Key", command=self.generate_key
        )  # Button to generate a shared key
        self.generate_key_button.grid(
            row=3, column=0, columnspan=2
        )  # Grid layout position

        # Button to perform encryption
        self.encrypt_button = tk.Button(
            root, text="Encrypt Text", command=self.encrypt_text
        )
        self.encrypt_button.grid(row=5, column=0)  # Grid layout position

        # Button to perform decryption
        self.decrypt_button = tk.Button(
            root, text="Decrypt Text", command=self.decrypt_text
        )
        self.decrypt_button.grid(row=5, column=1)  # Grid layout position

        # Create a combo box to choose encryption method (AES-256, Triple DES, or ChaCha20Poly1305)
        # Label for encryption method selection
        self.encryption_method_label = tk.Label(root, text="Encryption Method:")
        self.encryption_method_label.grid(
            row=6, column=0, columnspan=2
        )  # Grid layout position
        # Variable to store the selected encryption method
        self.encryption_method_var = tk.StringVar()
        self.encryption_method_var.set("AES-256")  # Default selection
        self.encryption_method_combo = tk.OptionMenu(
            root,
            self.encryption_method_var,
            "AES-256",
            "Triple DES",
            "ChaCha20Poly1305",
        )  # Combo box for method selection
        self.encryption_method_combo.grid(
            row=7, column=0, columnspan=2
        )  # Grid layout position

        self.key = None  # Initialize the shared key as None
        self.nonce = None  # For ChaCha20Poly1305

    def generate_key(self):
        # Generate a shared key using Fernet
        self.key = Fernet.generate_key()
        # Display the generated key
        self.shared_key_label.config(text=f"Shared Key: {self.key.decode()}")

    def generate_nonce(self):
        # Generate a random 16-byte nonce for ChaCha20Poly1305
        self.nonce = os.urandom(16)

    def encrypt_text(self):
        if self.key:
            text = (
                self.plain_text_input.get()
            )  # Get the plain text from the input field
            # Get the selected encryption method
            encryption_method = self.encryption_method_var.get()

            # Choose the appropriate encryption algorithm based on the selected method
            if encryption_method == "AES-256":
                cipher = Cipher(
                    algorithms.AES(self.key[:32]),
                    modes.ECB(),
                    backend=default_backend(),
                )
            elif encryption_method == "Triple DES":
                cipher = Cipher(
                    algorithms.TripleDES(self.key[:24]),
                    modes.ECB(),
                    backend=default_backend(),
                )
            elif encryption_method == "ChaCha20Poly1305":
                self.generate_nonce()  # Generate a nonce for ChaCha20Poly1305
                cipher = Cipher(
                    algorithms.ChaCha20(self.key[:32], nonce=self.nonce),
                    mode=None,
                    backend=default_backend(),
                )

            encryptor = cipher.encryptor()  # Create an encryptor
            # Add padding to ensure fixed block size
            padder = padding.PKCS7(128).padder()
            # Apply padding to the data
            padded_data = padder.update(text.encode()) + padder.finalize()
            encrypted_text = (
                encryptor.update(padded_data) + encryptor.finalize()
            )  # Encrypt the data

            self.encrypted_text_label.config(
                text=f"Encrypted Text: {encrypted_text.hex()}"
            )  # Display the encrypted text

    def decrypt_text(self):
        if self.key:
            encrypted_text = bytes.fromhex(
                self.encrypted_text_label.cget("text")[15:]
            )  # Get the encrypted text from the label
            # Get the selected encryption method
            encryption_method = self.encryption_method_var.get()

            # Choose the appropriate decryption algorithm based on the selected method
            if encryption_method == "AES-256":
                cipher = Cipher(
                    algorithms.AES(self.key[:32]),
                    modes.ECB(),
                    backend=default_backend(),
                )
            elif encryption_method == "Triple DES":
                cipher = Cipher(
                    algorithms.TripleDES(self.key[:24]),
                    modes.ECB(),
                    backend=default_backend(),
                )
            elif encryption_method == "ChaCha20Poly1305":
                cipher = Cipher(
                    algorithms.ChaCha20(self.key[:32], nonce=self.nonce),
                    mode=None,
                    backend=default_backend(),
                )

            decryptor = cipher.decryptor()  # Create a decryptor
            decrypted_data = (
                decryptor.update(encrypted_text) + decryptor.finalize()
            )  # Decrypt the data
            unpadder = padding.PKCS7(128).unpadder()  # Remove padding
            unpadded_data = (
                unpadder.update(decrypted_data) + unpadder.finalize()
            )  # Unpad the data
            decrypted_text = (
                unpadded_data.decode()
            )  # Convert the decrypted data to text

            self.decrypted_text_label.config(
                text=f"Decrypted Text: {decrypted_text}"
            )  # Display the decrypted text


# Main entry point of the program
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = EncryptionApp(root)  # Create an instance of the EncryptionApp class
    root.mainloop()  # Start the Tkinter main event loop
