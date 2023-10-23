# Import the tkinter library for creating the GUI
# and the cryptography library for encryption.
import tkinter as tk
from cryptography.fernet import Fernet

# Create a class called EncryptionApp to manage the application.


class EncryptionApp:
    def __init__(self, root):
        # Initialize the application and set its title.
        self.root = root
        self.root.title("Encryption App")

        # Initialize the key variable to None.
        self.key = None

        self.create_widgets()

    # Function to generate a random encryption key.
    def generate_key(self):
        self.key = Fernet.generate_key()  # Generate a key using Fernet.
        # Display the key in the label.
        self.shared_key_label.config(text=f"Shared Key: {self.key.decode()}")

    # Function to encrypt the text.
    def encrypt_text(self):
        if self.key:
            # Get the text from the input textbox.
            text = self.plain_text_input.get()
            fernet = Fernet(self.key)  # Create a Fernet cipher with the key.
            encrypted_text = fernet.encrypt(text.encode())  # Encrypt the text.
            # Display encrypted text.
            self.encrypted_text_label.config(
                text=f"Encrypted Text: {encrypted_text.decode()}")

    # Function to decrypt the encrypted text.
    def decrypt_text(self):
        if self.key:
            # Get the encrypted text from the label.
            encrypted_text = self.encrypted_text_label.cget("text")[15:]
            fernet = Fernet(self.key)  # Create a Fernet cipher with the key.
            # Decrypt the text.
            decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
            # Display decrypted text.
            self.decrypted_text_label.config(
                text=f"Decrypted Text: {decrypted_text}")

    def create_widgets(self):
        # Create and place widgets using grid layout
        self.shared_key_label = tk.Label(root, text="Shared Key:")
        self.shared_key_label.grid(row=0, column=0, columnspan=2)

        self.plain_text_input = tk.Entry(root, width=40)
        self.plain_text_input.grid(row=1, column=0, columnspan=2)

        self.encrypted_text_label = tk.Label(root, text="Encrypted Text:")
        self.encrypted_text_label.grid(row=2, column=0, columnspan=2)

        self.decrypted_text_label = tk.Label(root, text="Decrypted Text:")
        self.decrypted_text_label.grid(row=4, column=0, columnspan=2)

        self.generate_key_button = tk.Button(
            root, text="Generate Shared Key", command=self.generate_key)
        self.generate_key_button.grid(row=3, column=0, columnspan=2)

        self.encrypt_button = tk.Button(
            root, text="Encrypt Text", command=self.encrypt_text)
        self.encrypt_button.grid(row=5, column=0)

        self.decrypt_button = tk.Button(
            root, text="Decrypt Text", command=self.decrypt_text)
        self.decrypt_button.grid(row=5, column=1)


# Entry point of the program.
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window.
    app = EncryptionApp(root)  # Create an instance of the EncryptionApp class.
    root.mainloop()  # Start the GUI event loop.
