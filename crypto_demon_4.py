#!/usr/bin/env python3
"""
    Name: crypto_demon.py
    Author: 
    Created:
    Purpose: Encrypt and decrypt messages
"""

import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.poly1305 import Poly1305
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
import os
# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes


class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Crypto Demon")
        self.root.geometry("535x385+250+250")
        self.root.iconbitmap("encryption.ico")
        self.key = None
        # For ChaCha20Poly1305
        self.nonce = None
        self.var_encryption_method = tk.StringVar()
        # Set default selection
        self.var_encryption_method.set("AES-256")
        self.create_widgets()

# ------------------ GENERATE SHARED KEY ----------------------------------#
    def generate_key(self):
        """Generate shared key"""
        # Generates a cryptographically secure random sequence of bytes.
        # This sequence of bytes is of a fixed length
        # It contains a sufficient amount of entropy (randomness)
        # to make it very difficult for an attacker to predict or guess.
        self.key = Fernet.generate_key()

        # Decode the key to text to display in label
        self.lbl_shared_key.config(text=f"{self.key.decode()}")

# ------------------ GENERATE NONCE FOR CHACHA ----------------------------#
    def generate_nonce(self):
        """Generate a random 16-byte nonce for ChaCha20Poly1305"""
        # nonce is a number used once
        # urandom(16) generates random bytes of the specified length,
        # in this case 16 bytes. These bytes are generated
        # using a cryptographically secure random number generator
        # provided by the operating system.
        self.nonce = os.urandom(16)

# ------------------------- ENCRYPT TEXT ----------------------------------#
    def encrypt_text(self):
        """Encrypt text"""
        if self.key:
            self.text = self.plain_text_input.get(1.0, tk.END)
            encryption_method = self.var_encryption_method.get()

            if encryption_method == "AES-256":
                cipher = Cipher(algorithms.AES(
                    self.key[:32]), modes.ECB(), backend=default_backend())
            elif encryption_method == "Triple DES":
                cipher = Cipher(algorithms.TripleDES(
                    self.key[:24]), modes.ECB(), backend=default_backend())
            elif encryption_method == "ChaCha20":
                # Generate a nonce for ChaCha20Poly1305
                self.generate_nonce()
                cipher = Cipher(algorithms.ChaCha20(
                    self.key[:32], nonce=self.nonce
                ), mode=None, backend=default_backend())
            elif encryption_method == "DES":
                self.des_encrypt()

            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(text.encode()) + padder.finalize()
            encrypted_text = encryptor.update(
                padded_data) + encryptor.finalize()

            self.lbl_encrypted_text.config(
                text=f"{encrypted_text.hex()}")

# ------------------------- DES ENCRYPT -----------------------------------#
    def des_encrypt(self):
        # Create a DES key (must be 8 bytes)
        key = get_random_bytes(8)
        # Create a DES cipher object using the key
        # and the Electronic Codebook (ECB) mode.
        cipher = DES.new(key, DES.MODE_ECB)

        # Data to encrypt
        data = bytes(self.text, "utf-8")

        # Padding the data to be a multiple of 8 bytes (DES block size)
        padding_length = 8 - (len(data) % 8)
        data += bytes([padding_length]) * padding_length

        # Encrypt the data using the DES cipher
        encrypted_text = cipher.encrypt(data)
        self.lbl_encrypted_text.config(
            text=f"{encrypted_text.hex()}")

# ------------------------- DECRYPT TEXT ----------------------------------#
    def decrypt_text(self):
        """Decrypt text"""
        if self.key:
            encrypted_text = bytes.fromhex(
                self.lbl_encrypted_text.cget("text")
            )
            encryption_method = self.var_encryption_method.get()

            if encryption_method == "AES-256":
                cipher = Cipher(algorithms.AES(
                    self.key[:32]), modes.ECB(), backend=default_backend())
            elif encryption_method == "Triple DES":
                cipher = Cipher(algorithms.TripleDES(
                    self.key[:24]), modes.ECB(), backend=default_backend())
            elif encryption_method == "ChaCha20":
                cipher = Cipher(algorithms.ChaCha20(
                    self.key[:32], nonce=self.nonce),
                    mode=None, backend=default_backend())

            decryptor = cipher.decryptor()
            decrypted_data = decryptor.update(
                encrypted_text) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_data = unpadder.update(
                decrypted_data) + unpadder.finalize()
            decrypted_text = unpadded_data.decode()

            self.lbl_decrypted_text.config(
                text=f"{decrypted_text}")

# ----------------------- CREATE WIDGETS ----------------------------------#
    def create_widgets(self):
        """Create and place widgets using grid layout"""
        self.encryption_frame = ttk.Frame(root)
        self.encryption_frame.grid(row=0, column=1)

        self.encryption_method_label = ttk.Label(
            root, text="Encryption Method:")
        self.encryption_method_label.grid(row=0, column=0, sticky=tk.E)

        self.aes_radio = ttk.Radiobutton(
            self.encryption_frame, text="AES-256    ",
            variable=self.var_encryption_method, value="AES-256")
        
        self.des_radio = ttk.Radiobutton(
            self.encryption_frame, text="DES     ",
            variable=self.var_encryption_method, value="DES")
        
        self.three_des_radio = ttk.Radiobutton(
            self.encryption_frame, text="Triple DES    ",
            variable=self.var_encryption_method, value="Triple DES")
        
        self.cha_radio = ttk.Radiobutton(
            self.encryption_frame, text="ChaCha20",
            variable=self.var_encryption_method, value="ChaCha20")
        
        # Place the radio buttons in the frame using the grid layout
        self.aes_radio.grid(row=0, column=0, sticky=tk.W)
        self.des_radio.grid(row=0, column=1, sticky=tk.W)
        self.three_des_radio.grid(row=0, column=2, sticky=tk.W)
        self.cha_radio.grid(row=0, column=3, sticky=tk.W)
        # # Create a combo box to choose encryption method
        # # (AES-256, Triple DES, or ChaCha20Poly1305)
        # self.encryption_method_combo = ttk.OptionMenu(
        #     root,
        #     self.encryption_method_var,
        #     "AES-256", "Triple DES", "ChaCha20Poly1305"

        # )
        # self.encryption_method_combo.grid(row=0, column=1, sticky=tk.W)

        self.lbl_plain_text = tk.Label(root, text="Plain Text:")
        self.lbl_plain_text.grid(row=2, column=0, sticky=tk.E)

        self.plain_text_input = tk.Text(root, width=44, height=4)
        self.plain_text_input.grid(row=2, column=1, sticky=tk.W)

        self.btn_generate_key = ttk.Button(
            root, text="Generate Shared Key",
            command=self.generate_key)
        self.btn_generate_key.grid(row=3, column=0, sticky=tk.E)

        self.lbl_shared_key = tk.Label(
            root, relief=tk.GROOVE, anchor=tk.W, width=50)
        self.lbl_shared_key.grid(row=3, column=1)

        self.btn_encrypt = ttk.Button(
            root, text="Encrypt Text", command=self.encrypt_text)
        self.btn_encrypt.grid(row=4, column=0, sticky=tk.E)

        self.lbl_encrypted_text = tk.Label(
            root, relief=tk.GROOVE, anchor=tk.NW, width=50, height=4)
        self.lbl_encrypted_text.grid(row=4, column=1)

        self.btn_decrypt = ttk.Button(
            root, text="Decrypt Text", command=self.decrypt_text)
        self.btn_decrypt.grid(row=5, column=0, sticky=tk.E)

        self.lbl_decrypted_text = tk.Label(
            root, relief=tk.GROOVE, anchor=tk.NW, width=50, height=4)
        self.lbl_decrypted_text.grid(row=5, column=1)

        for child in self.root.winfo_children():
            child.grid_configure(padx=10, pady=10, ipadx=3, ipady=3)


if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()
