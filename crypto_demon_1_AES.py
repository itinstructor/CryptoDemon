#!/usr/bin/env python3
"""
    Name: crypto_demon_1_AES.py
    Author: 
    Created:
    Purpose: Encrypt and decrypt messages using AES
"""
# Import the tkinter library for creating the GUI
import tkinter as tk
# Import the cryptography library for encryption.
from cryptography.fernet import Fernet


class EncryptionApp:
    def __init__(self, root):
        # Initialize the key variable to None.
        self.key = None

        # Initialize the application and set its title.
        self.root = root
        self.root.title("Encryption App")

        self.create_widgets()

# ------------------------- GENERATE KEY ----------------------------------#
    def generate_key(self):
        """
        Generate random encryption key using the Fernet library
          and display it in a label.

        Flow:
        1. Generate random encryption key in bytes 
          using Fernet.generate_key() function.
        2. Store the generated key in the self.key variable.
        3. Decode the key from bytes to text display it in the label
        """
        # Generate a random encryption key in bytes using Fernet
        self.key = Fernet.generate_key()

        # Decode the key from bytes, display the key in the label
        self.lbl_shared_key.config(text=f"Shared Key: {self.key.decode()}")

# ------------------------- ENCRYPT TEXT ----------------------------------#
    def encrypt_text(self):
        """
        Encrypts the text entered in the input textbox using
          a Fernet cipher with a pre-generated encryption key.

        Inputs:
        - self: The instance of the EncryptionApp class.
        - self.key: The encryption key generated using generate_key method.
        - text: The text entered in the input textbox.

        Flow:
        1. Check if the encryption key (self.key) exists.
        2. Get the text from the input textbox.
        3. Create a Fernet cipher using the encryption key.
        4. Encode the input text to bytes.
        5. Encrypt the text using the Fernet cipher.
        6. Decode the encrypted text from bytes.
        7. Update the text of encrypted_text_label with the encrypted text.

        Outputs:
        - The encrypted text is displayed in the encrypted_text_label widget.
        """
        if self.key:
            # Get the text from the input textbox.
            text = self.entry.get()

            # Create a Fernet cipher with the key.
            fernet = Fernet(self.key)

            # Encode the input text to bytes
            # Encrypt the text.
            encrypted_text = fernet.encrypt(text.encode())

            # Decode the text from bytes, display encrypted text
            self.lbl_encrypted_text.config(
                text=f"Encrypted Text: {encrypted_text.decode()}")

# ------------------------- DECRYPT TEXT ----------------------------------#
    def decrypt_text(self):
        """
        Decrypts the text that has been encrypted using
          a Fernet cipher with a pre-generated encryption key.

        Inputs:
        - self: The instance of the EncryptionApp class.
        - self.key: Encryption key generated using the generate_key method.

        Flow:
        1. Check if the encryption key (self.key) exists.
        2. Get the encrypted text from the label.
        3. Create a Fernet cipher with the encryption key.
        4. Decrypt the encrypted text using the Fernet cipher.
        5. Decode the decrypted text from bytes to text.
        6. Update the text of the lbl_decrypted_text label with the decrypted text.

        Outputs:
        - The decrypted text is displayed in the lbl_decrypted_text widget.
        """
        if self.key:
            # Get the encrypted text from the label.
            encrypted_text = self.lbl_encrypted_text.cget("text")[15:]
            fernet = Fernet(self.key)  # Create a Fernet cipher with the key.
            # Decrypt the text.
            decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
            # Display decrypted text.
            self.lbl_decrypted_text.config(
                text=f"Decrypted Text: {decrypted_text}")

# ------------------------- CREATE WIDGETS --------------------------------#
    def create_widgets(self):
        # Create and place widgets using grid layout
        self.lbl_shared_key = tk.Label(root, text="Shared Key:")
        self.lbl_shared_key.grid(row=0, column=0, columnspan=2)

        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=1, column=0, columnspan=2)

        self.lbl_encrypted_text = tk.Label(root, text="Encrypted Text:")
        self.lbl_encrypted_text.grid(row=2, column=0, columnspan=2)

        self.lbl_decrypted_text = tk.Label(root, text="Decrypted Text:")
        self.lbl_decrypted_text.grid(row=4, column=0, columnspan=2)

        self.btn_generate_key = tk.Button(
            root, text="Generate Shared Key", command=self.generate_key)
        self.btn_generate_key.grid(row=3, column=0, columnspan=2)

        self.btn_encrypt = tk.Button(
            root, text="Encrypt Text", command=self.encrypt_text)
        self.btn_encrypt.grid(row=5, column=0)

        self.btn_decrypt = tk.Button(
            root, text="Decrypt Text", command=self.decrypt_text)
        self.btn_decrypt.grid(row=5, column=1)


# Entry point of the program.
if __name__ == "__main__":
    # Create the main application window.
    root = tk.Tk()
    # Create an instance of the EncryptionApp class.
    app = EncryptionApp(root)
    # Start the GUI event loop.
    root.mainloop()
