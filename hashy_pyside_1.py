import sys
import hashlib
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, \
    QFileDialog, QComboBox, QCheckBox

class HashCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hash Calculator")
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.text = ""

        # Create and layout widgets
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        # Text source selection (User Entry or From File)
        self.text_source_combo = QComboBox()
        self.text_source_combo.addItems(["User Entry", "From File"])
        layout.addWidget(self.text_source_combo)

        # Input text entry
        self.input_text = QLineEdit()
        layout.addWidget(self.input_text)

        # File path entry and open file button
        self.file_path_entry = QLineEdit()
        layout.addWidget(self.file_path_entry)
        self.open_file_button = QPushButton("Open Text File")
        self.open_file_button.clicked.connect(self.open_text_file)
        layout.addWidget(self.open_file_button)

        # Hash algorithm checkboxes and result labels
        self.checkboxes = {}
        self.result_labels = {}
        for algorithm in sorted(["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512",
                                "SHA3_224", "SHA3_256", "SHA3_384", "SHA3_512",
                                "Blake2b", "Blake2s", "Shake_128", "Shake_256",
                                "Whirlpool", "RIPEMD-256"]):
            checkbox = QCheckBox(algorithm)
            layout.addWidget(checkbox)
            self.checkboxes[algorithm] = checkbox
            result_label = QLabel()
            layout.addWidget(result_label)
            self.result_labels[algorithm] = result_label

        # Compute Hashes button
        compute_button = QPushButton("Compute Hashes")
        compute_button.clicked.connect(self.compute_hashes)
        layout.addWidget(compute_button)

        # Result label for displaying hash calculation results
        self.result_label = QLabel()
        layout.addWidget(self.result_label)

        # Save Hashes to File button
        save_button = QPushButton("Save Hashes to File")
        save_button.clicked.connect(self.save_hashes)
        layout.addWidget(save_button)

    def compute_hashes(self):
        text_source = self.text_source_combo.currentText()

        if text_source == "User Entry":
            self.text = self.input_text.text()
        elif text_source == "From File":
            file_path = self.file_path_entry.text()
            try:
                with open(file_path, 'r') as file:
                    self.text = file.read()
            except FileNotFoundError:
                self.result_label.setText("File not found.")
                return
        else:
            self.result_label.setText("Invalid text source.")
            return

        self.result_label.clear()

        for algorithm, checkbox in self.checkboxes.items():
            if checkbox.isChecked():
                hash_value = self.compute_hash(self.text, algorithm)
                self.result_labels[algorithm].setText(f"{algorithm}: {hash_value}")

    def compute_hash(self, text, algorithm):
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
        elif algorithm == "Shake_128":
            return hashlib.shake_128(text.encode()).hexdigest()
        elif algorithm == "Shake_256":
            return hashlib.shake_256(text.encode()).hexdigest()
        elif algorithm == "Whirlpool":
            return hashlib.new('whirlpool', text.encode()).hexdigest()
        elif algorithm == "RIPEMD-256":
            return hashlib.new('ripemd256', text.encode()).hexdigest()
        else:
            return ""

    def save_hashes(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Hashes to File", "", "Text files (*.txt);;All Files (*)", options=options)

        if file_path:
            with open(file_path, 'w') as file:
                for algorithm, checkbox in self.checkboxes.items():
                    if checkbox.isChecked():
                        hash_value = self.compute_hash(self.text, algorithm)
                        file.write(f"{algorithm}: {hash_value}\n")

            self.result_label.setText("Hashes saved to file.")

    def open_text_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text files (*.txt);;All Files (*)", options=options)

        if file_path:
            self.file_path_entry.setText(file_path)

def main():
    app = QApplication(sys.argv)
    window = HashCalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
