# picoCTF - ASCII Numbers

## Challenge Information

| Field      | Details                              |
| ---------- | ------------------------------------ |
| Platform   | picoCTF                              |
| Category   | General Skills                       |
| Difficulty | Medium                               |
| Skills     | Encoding, ASCII, Data Representation |

---

# Overview

ASCII Numbers is a challenge focused on understanding how data can be represented using different encoding formats.

The challenge requires converting numerical values into their corresponding ASCII characters to reveal the hidden message.

The attack path includes:

* Analyzing encoded data
* Understanding ASCII representation
* Converting numbers to characters
* Recovering the flag

---

# Reconnaissance

The challenge provides a sequence of numerical values.

Example:

```text id="8w3x5p"
80 105 99 111
```

These values represent ASCII character codes.

---

# Data Analysis

ASCII assigns numerical values to characters.

For example:

```text id="2m7q9v"
65 = A
66 = B
97 = a
```

The provided numbers were converted from decimal values into their corresponding ASCII characters.

---

# Exploitation

The conversion process was automated using command-line tools or a simple script.

Example Python solution:

```python id="6v1n4x"
numbers = [80,105,99,111]

flag = ""

for number in numbers:
    flag += chr(number)

print(flag)
```

The script converts each numerical value into its ASCII character representation.

---

# Flag Retrieval

After converting all ASCII values, the hidden text containing the flag was revealed.

---

# Tools Used

* Python
* ASCII reference table
* Linux terminal

---

# Skills Demonstrated

## Data Encoding

Understanding different ways information can be represented.

## Python Scripting

Automating repetitive conversion tasks.

## Problem Solving

Recognizing patterns in encoded data.

---

# Lessons Learned

* Data is often hidden through simple encoding techniques.
* Understanding character encoding is useful in security analysis.
* Small scripts can automate manual decoding tasks.
* Basic programming knowledge is valuable for CTF challenges.
