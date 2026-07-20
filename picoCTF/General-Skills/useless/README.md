# picoCTF - useless

## Challenge Information

| Field      | Details                                       |
| ---------- | --------------------------------------------- |
| Platform   | picoCTF                                       |
| Category   | General Skills                                |
| Difficulty | Medium                                        |
| Skills     | SSH, Linux Permissions, Command-Line Analysis |

---

# Overview

useless is a challenge focused on Linux command-line usage, remote access, and understanding file permissions.

The challenge demonstrates the importance of knowing Linux utilities and how misconfigurations or overlooked functionality can expose sensitive information.

The attack path includes:

* Connecting through SSH
* Inspecting available files and permissions
* Analyzing command behavior
* Recovering the flag

---

# Reconnaissance

The challenge provides SSH access information.

The connection was established using:

```bash id="8c4z1m"
ssh <username>@<host> -p <port>
```

After authentication, the available files and commands were inspected.

---

# System Enumeration

Basic Linux enumeration was performed.

Checking the current user:

```bash id="3k7p5v"
whoami
```

Listing files:

```bash id="1n8x4q"
ls -la
```

The directory contents revealed files and commands that required further analysis.

---

# Command Analysis

A suspicious command or script was identified.

The behavior of the command was investigated using Linux utilities and manual inspection.

The goal was understanding what the program actually executed and how it processed input.

---

# Exploitation

The discovered functionality was used to access the required information.

The challenge demonstrated that Linux commands may contain unexpected behavior depending on:

* Permissions
* Arguments
* Configuration
* Execution context

---

# Flag Retrieval

After analyzing the available commands and their behavior, the flag was recovered.

---

# Tools Used

* SSH
* Linux terminal
* ls
* file
* cat
* chmod

---

# Skills Demonstrated

## Linux Administration

Understanding files, permissions, and command execution.

## SSH Usage

Working with remote Linux environments.

## Command Analysis

Investigating unexpected behavior in programs and utilities.
