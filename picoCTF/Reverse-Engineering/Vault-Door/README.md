# picoCTF - Vault Door

## Challenge Information

| Field      | Details                                                 |
| ---------- | ------------------------------------------------------- |
| Platform   | picoCTF                                                 |
| Category   | Reverse Engineering                                     |
| Difficulty | Easy                                                    |
| Skills     | Source Code Analysis, Logic Analysis, Password Recovery |

---

# Overview

Vault Door is an introductory reverse engineering challenge focused on analyzing application source code to recover a hidden password.

The challenge demonstrates how security researchers analyze software logic to understand authentication mechanisms and identify exposed secrets.

The attack path includes:

* Reviewing the provided source code
* Analyzing password validation logic
* Recovering the expected input
* Verifying the solution

---

# Reconnaissance

The challenge provides a Java source code file.

The source code was inspected:

```bash
cat VaultDoor.java
```

The program contained a password validation function responsible for checking user input.

---

# Code Analysis

The authentication logic was analyzed to determine how the password was verified.

The program contained a hardcoded password comparison:

```java
if (password.equals(correct_password)) {
    unlock();
}
```

The expected password was stored directly inside the application logic.

---

# Solution

The source code was analyzed to recover the correct password value.

The password was extracted from the validation logic and provided as input to the program.

Example:

```bash
java VaultDoor
```

The recovered password successfully passed the verification function.

---

# Flag Retrieval

After entering the correct password, the program accepted the input and displayed the challenge flag.

---

# Tools Used

* Java source analysis
* Linux terminal
* Text editor

---

# Skills Demonstrated

## Static Analysis

Analyzing code without relying on execution behavior.

## Reverse Engineering

Understanding how software works by examining its internal logic.

## Authentication Analysis

Identifying weaknesses in local authentication mechanisms.

---

# Technical Concepts

## Hardcoded Secrets

Secrets stored directly inside source code can be recovered through:

* Source code exposure
* Reverse engineering
* Application analysis

## Static Analysis

Static analysis examines software artifacts without executing them, allowing researchers to identify logic flaws and exposed information.
