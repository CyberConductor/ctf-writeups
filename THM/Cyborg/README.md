# TryHackMe - Overpass 2 - Hacked

## Machine Information

| Field            | Details                                                               |
| ---------------- | --------------------------------------------------------------------- |
| Platform         | TryHackMe                                                             |
| Machine          | Overpass 2 - Hacked                                                   |
| Difficulty       | Easy                                                                  |
| Operating System | Linux                                                                 |
| Category         | Digital Forensics, Incident Response, Web Exploitation                |
| Main Skills      | PCAP analysis, log analysis, malware investigation, Linux enumeration |

---

# Overview

Overpass 2 - Hacked is a security investigation challenge focused on analyzing a compromise of a previously vulnerable system.

Unlike traditional exploitation-focused machines, this challenge focuses on understanding attacker activity by analyzing forensic evidence.

The challenge covers:

* Packet capture analysis
* Identifying attacker actions
* Extracting indicators of compromise
* Investigating malicious files
* Recovering attacker information

---

# Scenario

The Overpass team discovered that their infrastructure had been compromised.

A network capture and system artifacts were provided to investigate:

* How the attacker gained access
* What actions were performed
* What tools were used
* How the attacker maintained access

---

# PCAP Analysis

The provided packet capture was analyzed using Wireshark.

```bash
wireshark capture.pcap
```

Traffic analysis focused on:

* HTTP requests
* Suspicious connections
* File transfers
* Credentials

Filters used:

```text
http
```

and:

```text
tcp.stream
```

---

# Identifying Attacker Activity

The captured traffic revealed suspicious communication between the attacker and the compromised system.

The investigation uncovered:

* Attacker commands
* Downloaded files
* Reverse shell activity
* Malicious payloads

---

# File Extraction

Files transferred through network traffic were extracted.

Using Wireshark:

```
File → Export Objects → HTTP
```

Recovered files were analyzed.

---

# Malware Analysis

The extracted files were inspected using:

```bash
file <filename>
```

and:

```bash
strings <filename>
```

The analysis revealed indicators related to attacker persistence and execution methods.

---

# Hash Analysis

Suspicious files were hashed:

```bash
md5sum <file>
```

The hashes were analyzed to identify known malicious activity.

---

# System Investigation

Provided system information was reviewed to determine:

* Modified files
* User activity
* Attacker actions
* Persistence mechanisms

Logs and configuration files were inspected.

---

# Findings

The investigation revealed:

* Initial compromise details
* Attacker commands
* Malicious files introduced into the system
* Evidence of unauthorized access

---

# Tools Used

* Wireshark
* Linux command-line tools
* Strings
* File analysis tools
* Hash utilities

---

# Skills Practiced

## Digital Forensics

Analyzing evidence to reconstruct attacker behavior.

## Network Analysis

Understanding communication patterns and identifying malicious traffic.

## Incident Response

Investigating a compromise and identifying indicators of attack.
