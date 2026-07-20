# picoCTF - Plumbing

## Challenge Information

| Field      | Details                                             |
| ---------- | --------------------------------------------------- |
| Platform   | picoCTF                                             |
| Category   | General Skills                                      |
| Difficulty | Medium                                              |
| Skills     | Linux Command Line, Data Filtering, Text Processing |

---

# Overview

Plumbing is a challenge focused on using Linux command-line tools to process large amounts of text data efficiently.

The challenge demonstrates how powerful command-line utilities can be used during security assessments for searching, filtering, and analyzing information.

The attack path includes:

* Connecting to a remote service
* Receiving large amounts of output
* Filtering relevant information
* Extracting the flag

---

# Reconnaissance

The challenge provides access to a remote service.

The connection was established using:

```bash id="5d7s2h"
nc <challenge_host> <port>
```

The service returned a large amount of text data.

Manually searching through the output would be inefficient.

---

# Data Analysis

Linux text processing tools were used to analyze the returned information.

Useful commands include:

```bash id="8k3q1m"
grep
```

and:

```bash id="4x9p7v"
sort
uniq
```

The goal was to identify the line containing the flag format.

---

# Exploitation

The output from the remote service was piped into filtering commands.

Example:

```bash id="2n6m8q"
nc <host> <port> | grep pico
```

The command automatically searched the received data for the flag.

---

# Solution Approach

The challenge demonstrates the importance of efficient information processing.

Instead of manually reviewing thousands of lines, command-line tools were used to quickly locate the required information.

---

# Tools Used

* Netcat
* grep
* Linux command line
* Text processing utilities

---

# Skills Demonstrated

## Linux Fundamentals

Using command-line utilities for analysis.

## Data Filtering

Searching large datasets efficiently.

## Networking

Interacting with remote services using TCP connections.
