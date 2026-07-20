# picoCTF - Let's Warm Up

## Challenge Information

| Field      | Details                                    |
| ---------- | ------------------------------------------ |
| Platform   | picoCTF                                    |
| Category   | Other                                      |
| Difficulty | Easy                                       |
| Skills     | Hexadecimal, Data Representation, Encoding |

---

# Overview

Let's Warm Up is a beginner challenge focused on understanding hexadecimal representation.

The challenge introduces how computers represent values using different number systems and how hexadecimal values can be converted into readable formats.

The attack path includes:

* Identifying the hexadecimal value
* Converting the value into decimal
* Understanding character representation
* Recovering the flag

---

# Reconnaissance

The challenge provides a hexadecimal value.

The value was analyzed to determine its representation and required conversion.

Hexadecimal uses base 16:

```text id="b1f5wa"
0-9 and A-F
```

---

# Analysis

Hexadecimal values can represent characters through ASCII encoding.

Example:

```text id="k9v4cx"
0x41 = A
0x42 = B
```

The provided value was converted into the corresponding representation.

---

# Solution

The hexadecimal value was converted using standard conversion tools.

Example:

```bash id="6x8m3z"
echo $((16#value))
```

or:

```python id="0r5x8q"
int("value", 16)
```

The resulting value revealed the required information.

---

# Flag Retrieval

After converting the hexadecimal value correctly, the output contained the challenge flag.

---

# Tools Used

* Python
* Hexadecimal conversion tools
* Linux terminal

---

# Skills Demonstrated

## Data Representation

Understanding how numbers and characters are stored digitally.

## Hexadecimal Analysis

Converting and interpreting base-16 values.

## Encoding Fundamentals

Recognizing common data representation formats.

---

# Technical Concepts

## Hexadecimal

Hexadecimal is a base-16 numbering system commonly used in computing because it provides a compact representation of binary data.

## ASCII Encoding

ASCII maps numerical values to characters, allowing computers to represent text using numbers.
