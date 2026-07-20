# picoCTF - Mod 26

## Challenge Information

| Field      | Details                                        |
| ---------- | ---------------------------------------------- |
| Platform   | picoCTF                                        |
| Category   | Cryptography                                   |
| Difficulty | Easy                                           |
| Skills     | Encoding, ROT Cipher, Character Transformation |

---

# Overview

Mod 26 is a cryptography challenge focused on understanding alphabet-based transformations.

The challenge demonstrates how simple mathematical operations can be used to transform text and how these transformations can be reversed to recover the original message.

The attack path includes:

* Identifying the cipher type
* Understanding modular arithmetic
* Applying the reverse transformation
* Recovering the plaintext

---

# Reconnaissance

The challenge provides an encoded message.

The ciphertext was inspected to identify patterns:

* Alphabetic characters
* Repeated structures
* Possible substitution patterns

The use of alphabet positions suggested a Caesar-style transformation.

---

# Cryptographic Analysis

The cipher operates using modulo 26 arithmetic.

Each letter can be represented as a number:

```text id="94x3kj"
A = 0
B = 1
...
Z = 25
```

The transformation shifts characters within the alphabet range.

Encryption:

```text id="6h1m2r"
E(x) = (x + k) mod 26
```

Decryption reverses the shift:

```text id="3w8qvp"
D(x) = (x - k) mod 26
```

---

# Solution

The encoded text was decoded by reversing the alphabet transformation.

A simple script was used:

```python id="m4x1qz"
import string

alphabet = string.ascii_lowercase

# reverse the applied shift
```

The decoded output produced readable plaintext.

---

# Flag Retrieval

After applying the correct transformation, the plaintext revealed the challenge flag.

---

# Tools Used

* Python
* Alphabet mapping
* Linux terminal

---

# Skills Demonstrated

## Classical Cryptography

Understanding simple substitution and shift-based ciphers.

## Encoding Analysis

Recognizing patterns in transformed data.

## Python Automation

Using scripts to automate decoding operations.

---

# Technical Concepts

## Modular Arithmetic

Modulo operations allow values to wrap around a fixed range.

In alphabet ciphers, modulo 26 keeps transformations within the alphabet.

## Caesar Cipher

A Caesar cipher shifts each character by a fixed amount.

Although simple, it introduces the fundamentals of cryptographic transformations.
