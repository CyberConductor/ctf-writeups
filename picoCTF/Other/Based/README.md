# picoCTF - Based

## Challenge Information

| Field      | Details                                        |
| ---------- | ---------------------------------------------- |
| Platform   | picoCTF                                        |
| Category   | Other                                          |
| Difficulty | Easy                                           |
| Skills     | Encoding, Base Conversion, Data Representation |

---

# Overview

Based is a challenge focused on understanding different number systems and encoding formats.

The challenge demonstrates how information can be represented using different bases and how converting between representations can reveal hidden data.

The attack path includes:

* Identifying the encoding format
* Converting values between bases
* Decoding the final message
* Recovering the flag

---

# Reconnaissance

The challenge provides encoded data.

The format of the values was analyzed to determine the number system being used.

Common representations include:

* Binary (base 2)
* Decimal (base 10)
* Hexadecimal (base 16)

---

# Analysis

Different bases represent the same underlying value using different symbols.

Examples:

Binary:

```text
1010
```

Hexadecimal:

```text
0A
```

Decimal:

```text
10
```

The challenge required converting between these representations.

---

# Solution

The encoded values were converted into readable data.

Example commands:

```bash id="y4p8qm"
echo "value" | base64 -d
```

or using Python:

```python id="5x9m2v"
int(value, base)
```

The converted output revealed the hidden message.

---

# Flag Retrieval

After correctly converting the encoded values, the decoded message contained the challenge flag.

---

# Tools Used

* Python
* Base conversion tools
* Linux terminal

---

# Skills Demonstrated

## Data Representation

Understanding how computers represent information using different formats.

## Encoding Analysis

Identifying and decoding common data representations.

## Scripting

Automating repetitive conversion tasks.

---

# Technical Concepts

## Number Bases

A base defines how numbers are represented.

Common bases:

| Base | Name        |
| ---- | ----------- |
| 2    | Binary      |
| 10   | Decimal     |
| 16   | Hexadecimal |

## Encoding vs Encryption

Encoding changes data representation and is reversible without a secret key. It should not be considered a security mechanism.
