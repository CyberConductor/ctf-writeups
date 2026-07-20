# picoCTF - Vault Door 1

## Challenge Information

| Field      | Details                                                     |
| ---------- | ----------------------------------------------------------- |
| Platform   | picoCTF                                                     |
| Category   | Reverse Engineering                                         |
| Difficulty | Easy                                                        |
| Skills     | Source Code Analysis, String Reconstruction, Logic Analysis |

---

# Overview

Vault Door 1 is a reverse engineering challenge focused on analyzing how a program validates a password.

Instead of directly storing the password as a single string, the program checks individual characters against expected values.

The attack path includes:

* Reviewing the source code
* Understanding validation logic
* Reconstructing the password
* Testing the recovered input

---

# Reconnaissance

The challenge provides a Java source file.

The source code was inspected:

```bash id="7q3n5x"
cat VaultDoor1.java
```

The program contained a password verification function.

---

# Code Analysis

The password validation logic compared individual character positions.

Example:

```java id="8m2q7z"
password.charAt(0) == 'p'
password.charAt(1) == 'i'
```

Instead of storing the complete password, the application split the password into multiple character checks.

---

# Solution

The validation function was analyzed to recover:

* Character positions
* Expected characters
* Correct ordering

The characters were combined to reconstruct the complete password.

After entering the recovered password, the program accepted the input.

---

# Flag Retrieval

The correct password triggered the success condition and revealed the challenge flag.

---

# Tools Used

* Java source analysis
* Linux terminal
* Text editor

---

# Skills Demonstrated

## Static Code Analysis

Understanding program behavior by reading source code.

## Reverse Engineering

Recovering hidden information from application logic.

## Logic Reconstruction

Combining multiple validation checks to determine the expected input.

---

# Technical Concepts

## Password Validation

Applications should avoid storing sensitive authentication logic locally because attackers can analyze and recover hidden values.

## Source Code Exposure

When application logic is available, hardcoded checks and secrets can often be recovered through analysis.
