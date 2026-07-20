# picoCTF - Obedient Cat

## Challenge Information

| Field      | Details                                          |
| ---------- | ------------------------------------------------ |
| Platform   | picoCTF                                          |
| Category   | Other                                            |
| Difficulty | Easy                                             |
| Skills     | Linux Commands, File Handling, Basic Enumeration |

---

# Overview

Obedient Cat is a beginner Linux challenge focused on basic file handling and command-line usage.

The challenge introduces interacting with files in a Linux environment and demonstrates how simple commands can be used to retrieve information.

The attack path includes:

* Accessing the provided file
* Identifying file contents
* Reading the stored information
* Recovering the flag

---

# Reconnaissance

The challenge provides a file that contains the flag.

The file type was identified:

```bash id="9m4q2x"
file flag
```

The contents were inspected using standard Linux commands.

---

# File Analysis

The file was read using:

```bash id="2x8m7q"
cat flag
```

The command displays the contents of a file directly in the terminal.

Additional commands that can be used for file inspection:

```bash id="7v3k1m"
ls
```

and:

```bash id="4q8z5p"
less flag
```

---

# Solution

The provided file was opened using Linux command-line tools.

The content directly contained the required information.

---

# Flag Retrieval

Reading the file revealed the challenge flag.

---

# Tools Used

* Linux terminal
* file
* cat
* ls

---

# Skills Demonstrated

## Linux Fundamentals

Using basic commands to navigate and interact with files.

## File Analysis

Identifying and reading files in a command-line environment.

## Command-Line Usage

Understanding essential Linux utilities used in security environments.

---

# Technical Concepts

## Linux File Handling

Linux provides many command-line tools for managing and inspecting files.

Common commands:

| Command | Purpose               |
| ------- | --------------------- |
| ls      | List files            |
| cat     | Display file contents |
| file    | Identify file type    |
| less    | View file contents    |

## Command-Line Interfaces

Security professionals commonly use terminals for analysis, automation, and system investigation.
