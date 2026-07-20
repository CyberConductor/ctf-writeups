# picoCTF - Caesar

## Challenge Information

| Field      | Details                                                     |
| ---------- | ----------------------------------------------------------- |
| Platform   | picoCTF                                                     |
| Category   | Cryptography                                                |
| Difficulty | Easy                                                        |
| Skills     | Classical Cryptography, Caesar Cipher, Brute Force Analysis |

---

# Overview

Caesar is a cryptography challenge focused on decoding text encrypted using a Caesar cipher.

The challenge introduces one of the simplest substitution ciphers and demonstrates how encrypted messages can be recovered by understanding the transformation method.

The attack path includes:

* Identifying the cipher type
* Testing possible shifts
* Recovering readable plaintext
* Extracting the flag

---

# Reconnaissance

The challenge provides an encrypted message.

The ciphertext was analyzed for:

* Alphabetic characters
* Repeated patterns
* Possible substitution behavior

The fixed character shift pattern indicated that the message used a Caesar cipher.

---

# Cryptographic Analysis

The Caesar cipher shifts every letter by a fixed number of positions in the alphabet.

Example:

```text id="kz8s3v"
A → D
B → E
C → F
```

The encryption formula:

```text id="6n1q8m"
C = (P + k) mod 26
```

The decryption formula:

```text id="2m7v4x"
P = (C - k) mod 26
```

Where:

* `P` = plaintext
* `C` = ciphertext
* `k` = shift value

---

# Solution

Since Caesar ciphers only have a limited number of possible shifts, all possible rotations were tested.

A Python script was used to automate the process:

```python id="8j4m2s"
import string

alphabet = string.ascii_lowercase

for shift in range(26):
    decoded = ""

    for char in ciphertext:
        if char in alphabet:
            decoded += alphabet[(alphabet.index(char)-shift) % 26]
        else:
            decoded += char

    print(decoded)
```

The correct shift produced readable plaintext.

---

# Flag Retrieval

After identifying the correct Caesar shift, the decrypted message revealed the challenge flag.

---

# Tools Used

* Python
* Caesar cipher analysis
* Linux terminal

---

# Skills Demonstrated

## Classical Cryptography

Understanding basic substitution-based encryption.

## Brute Force Techniques

Testing possible solutions when the key space is small.

## Automation

Using scripts to quickly analyze encrypted data.

---

# Technical Concepts

## Caesar Cipher

A Caesar cipher is a substitution cipher where each letter is shifted by a fixed amount.

Because there are only 26 possible shifts, it can be easily brute-forced.

## Substitution Ciphers

Substitution ciphers replace characters according to a defined mapping, allowing encryption and decryption through transformations.
