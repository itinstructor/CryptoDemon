# CryptoDemon

Python Cryptography Demonstration Program

### Requirements
- [PyCryptodome](https://pypi.org/project/pycryptodome) is a self-contained Python package of low-level cryptographic primitives.

```pip install pycryptodome```

### Cryptography Modules

- (10/02/2023) **des3_class.py** uses 3DES to encrypt and decrypt data with or without a user input shared key
- (09/28/2023) **des3_class_shared_key.py** uses 3DES to encrypt and decrypt incoming plain text with user shared key
- (09/28/2023) **des3_generated_key.py** uses 3DES to encrypt and decrypt incoming plain text with random key

### DES Encryption

The Data Encryption Standard (DES) is a symmetric-key block cipher used in the field of cryptography and information security. It was developed in the 1970s and became a federal standard in the United States. DES operates on 64-bit blocks of data and uses a 56-bit encryption key.

DES is known for its historical significance as one of the earliest widely adopted encryption standards. It is no longer considered secure for modern applications due to advances in computing power. Its 56-bit key length makes it vulnerable to brute-force attacks, and it has been replaced by more robust encryption algorithms like Triple DES (3DES) and the Advanced Encryption Standard (AES).

DES uses a 56 bit key. The initial key consists of 64 bits (8 bytes). Before the DES process even starts, every 8th bit of the key is discarded to produce a 56-bit key. DES uses an 8 byte block cipher. Data is encrypted 64 bits (8 bytes) at a time and must be padded to increments of 8 bytes.

### 3DES Encryption
Triple Data Encryption Standard (3DES) is a symmetric-key block cipher used in information security and cryptography. It operates on 64-bit blocks of data and uses a key length of either 128, 192, or 256 bits. 3DES applies the DES algorithm three times consecutively to each data block, hence the name "triple."

Each block goes through an encryption-decryption-encryption process with three different keys derived from the original key. This triple application of DES significantly increases the security of the data compared to single DES.

3DES is widely used for securing sensitive information and has been a crucial cryptographic algorithm in various applications, including financial services and data protection. However, due to advances in computing power, it is considered somewhat outdated, and AES (Advanced Encryption Standard) is now preferred for most security-critical applications.

### About Me
I am an Information Technology Instructor at [Western Nebraska Community College](https://www.wncc.edu). I teach Information Technology, CyberSecurity and Computer Science. Best job ever!

Visit our Facebook page: [Facebook WNCC IT Program](https://www.facebook.com/wnccitprogram/)

### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Copyright (c) 2023 William A Loring