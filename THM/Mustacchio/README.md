# TryHackMe - Mustacchio

## Machine Information

| Field            | Details                                                              |
| ---------------- | -------------------------------------------------------------------- |
| Platform         | TryHackMe                                                            |
| Machine          | Mustacchio                                                           |
| Difficulty       | Easy                                                                 |
| Operating System | Linux                                                                |
| Category         | Web Exploitation, XML Security, Privilege Escalation                 |
| Main Skills      | Web enumeration, XML analysis, source code review, SUID exploitation |

---

# Overview

Mustacchio is a Linux-based challenge focused on identifying vulnerable web functionality and abusing insecure system configurations.

The attack path includes:

* Web reconnaissance
* Hidden endpoint discovery
* XML injection exploitation
* Source code analysis
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying available services.

## Nmap Scan

```bash id="8j2m4x"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="4g9v2s"
22/tcp SSH
80/tcp HTTP
8765/tcp HTTP
```

Multiple web services were discovered.

---

# Web Enumeration

Directory enumeration was performed on the discovered web services.

Using Gobuster:

```bash id="n7q5bx"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Additional directories and endpoints were discovered.

The secondary web service was investigated.

---

# Source Code Analysis

The website source code was reviewed for exposed information.

The analysis revealed:

* Hidden files
* Application details
* Potentially sensitive information

A backup file was discovered:

```text id="a3z7wq"
backupFile
```

The contents revealed useful information for further exploitation.

---

# XML Injection

The application contained a functionality that processed XML input.

The XML parser was vulnerable to external entity processing.

A crafted XML payload was used to test the vulnerability.

Example:

```xml id="p3y8xm"
<!DOCTYPE foo [
<!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
```

The vulnerability allowed reading local files from the server.

---

# Credential Discovery

Sensitive files were retrieved using the XML vulnerability.

The discovered information was used to obtain valid credentials.

---

# Initial Access

SSH access was obtained using the recovered credentials.

```bash id="q6w2mp"
ssh <username>@<TARGET_IP>
```

A shell on the target machine was obtained.

---

# Privilege Escalation

System enumeration was performed.

SUID binaries were searched:

```bash id="w4c8yn"
find / -perm -u=s -type f 2>/dev/null
```

A custom binary with elevated permissions was discovered.

The binary behavior was analyzed.

---

# Root Access

The vulnerable SUID binary was abused to execute commands with elevated privileges.

After successful exploitation:

```bash id="x8v3ms"
whoami
```

Output:

```text id="e2k9qa"
root
```

The root flag was retrieved.

---

# Tools Used

* Nmap
* Gobuster
* Burp Suite
* XML analysis tools
* SSH
* Linux enumeration tools

---

# Vulnerabilities Identified

## XML External Entity (XXE)

**Type:** XML Injection

**Impact:**

Allows attackers to read local files and potentially interact with internal resources.

---

## Exposed Backup Files

**Type:** Information Disclosure

**Impact:**

Accessible backup files can reveal sensitive application information.

---

## SUID Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect permissions can allow users to execute privileged operations.
