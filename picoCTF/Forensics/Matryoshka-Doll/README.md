# picoCTF - Matryoshka Doll

## Challenge Information

| Field      | Details                                       |
| ---------- | --------------------------------------------- |
| Platform   | picoCTF                                       |
| Category   | Forensics                                     |
| Difficulty | Medium                                        |
| Skills     | File Analysis, Steganography, Data Extraction |

---

# Overview

Matryoshka Doll is a forensics challenge focused on discovering hidden data inside files.

The challenge is based on the concept of a matryoshka doll, where one object contains another hidden object inside it. Similarly, the provided file contains multiple layers of embedded data.

The attack path includes:

* Identifying hidden file data
* Extracting embedded files
* Repeating the extraction process
* Recovering the final information

---

# Reconnaissance

The challenge provides an image file.

The file type was checked:

```bash id="v8j3rp"
file <filename>
```

The metadata and structure of the file were analyzed to identify unusual content.

---

# File Analysis

The file was inspected using:

```bash id="4j7hcx"
binwalk <filename>
```

Binwalk searches files for embedded content and identifies hidden files inside other files.

The output revealed additional data embedded within the original file.

---

# Data Extraction

The embedded content was extracted using:

```bash id="7y3zxa"
binwalk -e <filename>
```

The extraction produced another file.

The same analysis process was repeated:

```bash id="9x2mqa"
file extracted_file
binwalk extracted_file
```

Each layer contained another hidden file.

---

# Layered Extraction

The challenge required repeating the extraction process until reaching the final hidden data.

This demonstrates why forensic analysts must inspect files beyond their visible contents.

---

# Flag Retrieval

After extracting all embedded layers, the final file contained the challenge flag.

---

# Tools Used

* binwalk
* file
* Linux terminal
* Hex/file analysis tools

---

# Skills Demonstrated

## File Forensics

Analyzing files for hidden information.

## Steganography Concepts

Understanding how data can be hidden inside other files.

## Automated Analysis

Using tools to identify embedded content quickly.

---

# Forensic Concepts

## File Carving

Recovering embedded or hidden data from files based on known signatures.

## Embedded Data

Files may contain additional hidden information that is not visible during normal use.
