# TryHackMe - Agent Sudo

## Machine Information

| Field            | Details                                                                         |
| ---------------- | ------------------------------------------------------------------------------- |
| Platform         | TryHackMe                                                                       |
| Machine          | Agent Sudo                                                                      |
| Difficulty       | Easy                                                                            |
| Operating System | Linux                                                                           |
| Category         | Web Enumeration, Steganography, Privilege Escalation                            |
| Main Skills      | HTTP enumeration, user-agent manipulation, hidden data extraction, SSH analysis |

---

# Overview

Agent Sudo is a beginner-friendly Linux machine that focuses on discovering hidden information through web enumeration and exploiting weak security practices.

The challenge includes:

* Web reconnaissance
* HTTP header manipulation
* Hidden file discovery
* Password cracking
* Steganography analysis
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying exposed services on the target machine.

## Nmap Scan

```bash id="4r7q6c"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="0yx2bz"
21/tcp   FTP
22/tcp   SSH
80/tcp   HTTP
```

The web service was investigated further.

---

# Web Enumeration

The website contained a message referencing different user agents.

The application behavior suggested that the server response depended on the HTTP User-Agent header.

The request header was modified:

```http id="84m6dj"
User-Agent: C
```

Different values were tested to identify valid agents.

The correct agent value revealed additional information.

---

# User-Agent Discovery

Using custom HTTP headers:

```bash id="x7q8mn"
curl -A "Agent R" http://<TARGET_IP>
```

The response revealed a hidden username.

This information was used for further enumeration.

---

# FTP Enumeration

The FTP service was checked for anonymous access.

```bash id="w3k8pr"
ftp <TARGET_IP>
```

Accessible files were downloaded.

The files contained clues and additional information required for the next stage.

---

# Image Analysis

An image file was discovered during enumeration.

The file was analyzed for hidden information.

Metadata extraction:

```bash id="h8p3sd"
exiftool image.jpg
```

Hidden data was extracted using steganography tools.

Example:

```bash id="j5m9sa"
steghide extract -sf image.jpg
```

A password-protected archive was recovered.

---

# Password Cracking

The extracted password hash or archive password was cracked using John the Ripper.

Example:

```bash id="z8w4fk"
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

The recovered credentials allowed further access.

---

# SSH Access

Using the discovered credentials:

```bash id="t2m8vq"
ssh <username>@<TARGET_IP>
```

A shell on the target system was obtained.

---

# Privilege Escalation

System enumeration was performed after obtaining user access.

Information gathering:

```bash id="k4v6mz"
sudo -l
```

Additional files and permissions were reviewed.

The escalation path involved exploiting a misconfiguration in the system.

---

# Root Access

The privilege escalation method allowed execution of commands with elevated permissions.

After successful escalation:

```bash id="b5x9qa"
whoami
```

returned:

```text id="8n0v3f"
root
```

The root flag was retrieved from:

```text id="h2c6wm"
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* Curl
* FTP
* Exiftool
* Steghide
* John the Ripper
* SSH
* Linux enumeration tools

---

# Vulnerabilities Identified

## Information Disclosure Through HTTP Headers

**Type:** Information Disclosure

**Impact:**

Sensitive information was exposed through server responses based on manipulated request headers.

---

## Weak Credential Protection

**Type:** Credential Exposure

**Impact:**

Weak passwords allowed recovery through offline cracking techniques.

---

## Privilege Escalation Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect system configuration allowed a normal user to gain elevated privileges.

---

# Lessons Learned

* HTTP headers can reveal hidden functionality or information.
* Metadata and hidden content should always be reviewed during investigations.
* Password strength is critical because exposed credentials can often be cracked offline.
* Proper Linux permission management is essential to prevent privilege escalation.
