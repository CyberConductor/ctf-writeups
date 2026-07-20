# picoCTF - Advanced Potion

## Challenge Information

| Field      | Details                                         |
| ---------- | ----------------------------------------------- |
| Platform   | picoCTF                                         |
| Category   | Forensics                                       |
| Difficulty | Medium                                          |
| Skills     | File Analysis, Metadata Analysis, Data Recovery |

---

# Overview

Advanced Potion is a forensics challenge focused on investigating files and identifying hidden information through analysis.

The challenge demonstrates how digital investigators examine files beyond their visible content by analyzing metadata, structure, and embedded information.

The attack path includes:

* Inspecting provided files
* Analyzing metadata
* Identifying hidden information
* Recovering the flag

---

# Reconnaissance

The challenge provides a file that requires forensic investigation.

The first step was identifying the file type:

```bash id="j3d8aw"
file <filename>
```

This determines the actual format of the file and helps select appropriate analysis tools.

---

# File Metadata Analysis

The file metadata was inspected using:

```bash id="8q4j9x"
exiftool <filename>
```

Metadata can reveal information such as:

* Author details
* Software used
* Timestamps
* Embedded comments
* Additional file information

---

# File Structure Analysis

The file contents were analyzed to identify hidden data.

Additional tools were used depending on the file format:

```bash id="1w8z4q"
strings <filename>
```

This searches for readable text inside binary files.

---

# Data Extraction

The discovered information was analyzed and extracted from the file.

The hidden content contained the information required to retrieve the flag.

---

# Flag Retrieval

After completing the forensic analysis, the hidden flag was recovered.

---

# Tools Used

* file
* exiftool
* strings
* Linux terminal

---

# Skills Demonstrated

## Metadata Analysis

Understanding how files can contain hidden information.

## File Investigation

Analyzing files beyond their normal usage.

## Digital Evidence Handling

Extracting useful information from available artifacts.

---

# Forensic Concepts

## Metadata

Metadata is information stored alongside files that describes properties about the file.

Examples:

* Creation information
* Software information
* File attributes

## Strings Analysis

Extracting readable text from files can reveal:

* Credentials
* Hidden messages
* Configuration data

---

# Mitigation

To reduce information leakage:

* Remove unnecessary metadata before publishing files
* Sanitize uploaded files
* Restrict sensitive information in document properties
* Review files before sharing externally

---

# Lessons Learned

* Files often contain more information than what is visible.
* Metadata can reveal valuable forensic evidence.
* Simple tools can uncover hidden information quickly.
* File analysis is an important skill in security investigations.
