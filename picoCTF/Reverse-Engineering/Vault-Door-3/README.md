# picoCTF - Vault Door 3

## Challenge Information

| Field      | Details                                      |
| ---------- | -------------------------------------------- |
| Platform   | picoCTF                                      |
| Category   | Reverse Engineering                          |
| Difficulty | Medium                                       |
| Skills     | Code Analysis, Encoding, String Manipulation |

---

# Overview

Vault Door 3 is a reverse engineering challenge focused on analyzing a password validation function that uses encoding and transformation techniques.

The challenge demonstrates how developers may attempt to hide secrets through simple obfuscation methods and how reverse engineering can reveal the original data.

The attack path includes:

* Inspecting source code
* Understanding encoding functions
* Reversing string transformations
* Recovering the password

---

# Reconnaissance

The challenge provides a Java source code file.

The source was reviewed:

```bash id="4v9y7n"
cat VaultDoor3.java
```

The program contained a password checking function with multiple transformation steps.

---

# Code Analysis

The password was not stored directly.

The program performed operations such as:

* Character rearrangement
* String manipulation
* Encoding transformations

The validation logic transformed the user input and compared it against an expected value.

---

# Solution

The verification function was reversed step by step.

The process included:

1. Identifying the transformation operations
2. Understanding the order of operations
3. Reversing each transformation
4. Reconstructing the original password

The recovered password was then supplied to the program.

Example:

```bash id="m2k7vz"
java VaultDoor3
```

---

# Flag Retrieval

After providing the reconstructed password, the program accepted the input and returned the challenge flag.

---

# Tools Used

* Java source analysis
* Python scripting
* Linux terminal

---

# Skills Demonstrated

## Code Reversal

Understanding how transformations can be reversed to recover original data.

## Program Logic Analysis

Following execution flow to determine how input is processed.

## String Manipulation

Analyzing encoding and transformation functions.

---

# Technical Concepts

## Obfuscation

Obfuscation changes the appearance of code or data to make analysis harder but does not provide real security.

## Reverse Engineering

Reverse engineering allows analysts to understand software behavior by examining code, logic, and transformations.
