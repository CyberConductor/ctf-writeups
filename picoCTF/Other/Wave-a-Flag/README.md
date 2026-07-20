# picoCTF - Wave a Flag

## Challenge Information

| Field      | Details                                              |
| ---------- | ---------------------------------------------------- |
| Platform   | picoCTF                                              |
| Category   | Other                                                |
| Difficulty | Easy                                                 |
| Skills     | Linux Commands, File Analysis, Executable Inspection |

---

# Overview

Wave a Flag is a beginner challenge focused on analyzing executable files and discovering information stored inside them.

The challenge introduces basic binary inspection techniques and demonstrates how command-line tools can reveal useful information from files.

The attack path includes:

* Identifying the provided file
* Inspecting executable information
* Finding embedded data
* Recovering the flag

---

# Reconnaissance

The provided file was analyzed to determine its type:

```bash id="5q7m2x"
file warm
```

The output showed that the file was an executable binary.

---

# File Analysis

The binary was inspected using:

```bash id="8p4z1n"
strings warm
```

The `strings` command extracts readable text from binary files.

The output contained useful information related to the challenge.

---

# Solution

The binary was executed:

```bash id="3m9x6q"
./warm
```

The program displayed information needed to retrieve the flag.

Additional analysis using:

```bash id="1k5v8c"
strings warm | grep pico
```

helped locate the flag text inside the executable.

---

# Flag Retrieval

After inspecting and executing the binary, the challenge flag was obtained.

---

# Tools Used

* Linux terminal
* file
* strings
* Bash

---

# Skills Demonstrated

## Binary Inspection

Analyzing executable files for useful information.

## Linux Command Usage

Using common command-line tools for security analysis.

## Static Analysis

Extracting information from files without modifying them.

---

# Technical Concepts

## Strings Analysis

Binary files often contain readable text such as:

* Error messages
* Debug information
* Embedded data
* Configuration values

## Executable Analysis

Inspecting binaries is an important first step in reverse engineering and malware analysis.
