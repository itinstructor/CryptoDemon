#!/usr/bin/env python3
"""
    Name: hashy_2.py
    Author: 
    Created: 10/01/2023
    Purpose: 
"""
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import hashlib


# Create a class for our Hash Calculator application that inherits from tkinter's Tk class
class HashCalculatorApp(tk.Tk):
    def __init__(self):
        # Initialize the main application window
        super().__init__()
        # Set the title of the window
        self.title("Hash Calculator")

        # Initialize a variable to store the input text
        self.text = ""

        # Create and pack a combo box for selecting the text source (User Entry or From File)
        self.text_source_combo_label = tk.Label(self, text="Text Source:")
        self.text_source_combo_label.grid(row=0, column=0, sticky="w")
        self.text_source_combo = ttk.Combobox(
            self, values=["User Entry", "From File"])
        self.text_source_combo.set("User Entry")  # Set the default selection
        self.text_source_combo.grid(row=0, column=1, sticky="w")

        # Create and pack an input label and entry for entering text
        self.input_label = tk.Label(self, text="Enter Text:")
        self.input_label.grid(row=1, column=0, sticky="w")
        self.input_text = tk.Entry(self)
        self.input_text.grid(row=1, column=1, sticky="w")

        # Create and pack an entry for specifying a file path
        self.file_path_label = tk.Label(self, text="File Path:")
        self.file_path_label.grid(row=2, column=0, sticky="w")
        self.file_path_entry = tk.Entry(self)
        self.file_path_entry.grid(row=2, column=1, sticky="w")

        # Create and pack a button for opening a text file
        self.open_file_button = tk.Button(
            self, text="Open Text File", command=self.open_text_file)
        self.open_file_button.grid(row=2, column=2)

        # Create dictionaries to store checkboxes and result labels for various hash algorithms
        self.checkboxes = {}
        self.result_labels = {}
        # Start the grid from row 3
        row_index = 3

        # Create checkboxes for hash algorithms and associated result labels
        for algorithm in sorted(
            ["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512",
             "SHA3_224", "SHA3_256", "SHA3_384", "SHA3_512",
             "Blake2b", "Blake2s"]):
            # Create a variable to track the checkbox state
            self.checkboxes[algorithm] = tk.IntVar()
            # Create a checkbox widget with the text of the algorithm
            checkbox = tk.Checkbutton(
                self, text=algorithm, variable=self.checkboxes[algorithm])
            # Place the checkbox on the grid at the specified row and column
            checkbox.grid(row=row_index, column=0, sticky="w")
            # Create labels for displaying results and place them on the grid
            self.result_labels[algorithm] = tk.Label(
                self, text="", justify="left")
            self.result_labels[algorithm].grid(
                row=row_index, column=1, sticky="w")
            row_index += 1

        # Create a button for computing hashes and place it on the grid
        self.compute_button = tk.Button(
            self, text="Compute Hashes", command=self.compute_hashes)
        self.compute_button.grid(row=row_index, column=0, columnspan=2)

        # Create a label for displaying hash calculation results and place it on the grid
        self.result_label = tk.Label(
            self, text="", wraplength=300, justify="left")
        self.result_label.grid(row=row_index + 1, column=0, columnspan=2)

        # Create a button for saving hashes to a file and place it on the grid
        self.save_button = tk.Button(
            self, text="Save Hashes to File", command=self.save_hashes)
        self.save_button.grid(row=row_index + 2, column=0, columnspan=2)

    # Function to compute hashes
    def compute_hashes(self):
        # Get the selected text source (User Entry or From File)
        text_source = self.text_source_combo.get()

        # Depending on the selected source, retrieve the input text
        if text_source == "User Entry":
            self.text = self.input_text.get()
        elif text_source == "From File":
            file_path = self.file_path_entry.get()
            try:
                # Attempt to open and read text from the specified file
                with open(file_path, 'r') as file:
                    self.text = file.read()
            except FileNotFoundError:
                # Display an error message if the file is not found
                self.result_label.config(text="File not found.")
                return
        else:
            # Display an error message if an invalid text source is selected
            self.result_label.config(text="Invalid text source.")
            return

        # Clear previous results
        self.result_label.config(text="")

        # Loop through selected hash algorithms and calculate their hashes
        for algorithm, var in self.checkboxes.items():
            if var.get():
                hash_value = self.compute_hash(self.text, algorithm)
                self.result_labels[algorithm].config(
                    text=f"{algorithm}: {hash_value}")

    # Function to compute a specific hash
    def compute_hash(self, text, algorithm):
        # Use the hashlib library to compute the hash based on the selected algorithm
        if algorithm == "MD5":
            return hashlib.md5(text.encode()).hexdigest()
        elif algorithm == "SHA1":
            return hashlib.sha1(text.encode()).hexdigest()
        elif algorithm == "SHA224":
            return hashlib.sha224(text.encode()).hexdigest()
        elif algorithm == "SHA256":
            return hashlib.sha256(text.encode()).hexdigest()
        elif algorithm == "SHA384":
            return hashlib.sha384(text.encode()).hexdigest()
        elif algorithm == "SHA512":
            return hashlib.sha512(text.encode()).hexdigest()
        elif algorithm == "SHA3_224":
            return hashlib.sha3_224(text.encode()).hexdigest()
        elif algorithm == "SHA3_256":
            return hashlib.sha3_256(text.encode()).hexdigest()
        elif algorithm == "SHA3_384":
            return hashlib.sha3_384(text.encode()).hexdigest()
        elif algorithm == "SHA3_512":
            return hashlib.sha3_512(text.encode()).hexdigest()
        elif algorithm == "Blake2b":
            return hashlib.blake2b(text.encode()).hexdigest()
        elif algorithm == "Blake2s":
            return hashlib.blake2s(text.encode()).hexdigest()
        # elif algorithm == "Shake_128":
        #     return hashlib.shake_128(text.encode()).hexdigest()
        # elif algorithm == "Shake_256":
        #     return hashlib.shake_256(text.encode()).hexdigest()
        # elif algorithm == "Whirlpool":
        #     return hashlib.new('whirlpool', text.encode()).hexdigest()
        # elif algorithm == "RIPEMD-256":
        #     return hashlib.new('ripemd256', text.encode()).hexdigest()
        else:
            return ""  # Return an empty string for unsupported algorithms

    # Function to save hashes to a file
    def save_hashes(self):
        # Prompt the user to choose a file path for saving the hashes
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if not file_path:
            return  # If the user cancels the file dialog, do nothing

        # Write the calculated hashes to the chosen file
        with open(file_path, 'w') as file:
            for algorithm, var in self.checkboxes.items():
                if var.get():
                    hash_value = self.compute_hash(self.text, algorithm)
                    file.write(f"{algorithm}: {hash_value}\n")

        # Display a message indicating that the hashes have been saved
        self.result_label.config(text="Hashes saved to file.")

    # Function to open a text file
    def open_text_file(self):
        # Prompt the user to choose a text file to open
        file_path = filedialog.askopenfilename(
            filetypes=[("Text files", "*.txt")])
        if file_path:
            # Update the file path entry field with the chosen file path
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)


# Create an instance of the HashCalculatorApp class and start the main loop
if __name__ == "__main__":
    app = HashCalculatorApp()
    app.mainloop()
