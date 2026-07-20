# TryHackMe - Debug

## Machine Information

| Field            | Details                                                                            |
| ---------------- | ---------------------------------------------------------------------------------- |
| Platform         | TryHackMe                                                                          |
| Machine          | Debug                                                                              |
| Difficulty       | Medium                                                                             |
| Operating System | Linux                                                                              |
| Category         | Web Exploitation, PHP Deserialization, Privilege Escalation                        |
| Main Skills      | Web enumeration, PHP analysis, deserialization attacks, Linux privilege escalation |

---

# Overview

Debug is a Linux-based challenge focused on discovering vulnerabilities in a web application and exploiting unsafe handling of serialized data.

The challenge demonstrates:

* Web reconnaissance
* Hidden endpoint discovery
* PHP application analysis
* PHP object deserialization exploitation
* Privilege escalation

---

# Reconnaissance

The first step was identifying available services.

## Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text
22/tcp SSH
80/tcp HTTP
```

The web service was investigated further.

---

# Web Enumeration

Directory enumeration was performed:

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Several directories and files were discovered.

The application structure was analyzed to identify hidden functionality.

---

# Web Application Analysis

The application source code was reviewed.

The analysis revealed insecure handling of PHP serialized objects.

The application accepted serialized input without proper validation.

This allowed manipulation of object properties.

---

# PHP Deserialization Exploitation

PHP object serialization was analyzed to understand the application behavior.

The vulnerable functionality allowed an attacker to modify serialized objects and trigger unintended actions.

A crafted serialized payload was generated and submitted.

The vulnerability resulted in command execution on the target system.

---

# Initial Access

A reverse shell was obtained.

Listener:

```bash
nc -lvnp 4444
```

The shell was stabilized:

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

---

# User Enumeration

After obtaining access:

```bash
whoami
```

System information was collected:

```bash
uname -a
```

The user flag was located:

```text
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Sudo permissions were checked:

```bash
sudo -l
```

Additional system analysis was performed:

```bash
find / -perm -u=s -type f 2>/dev/null
```

A privilege escalation path was identified.

---

# Root Access

The discovered weakness was exploited to obtain elevated privileges.

Verification:

```bash
whoami
```

Output:

```text
root
```

The root flag was retrieved.

---

# Tools Used

* Nmap
* Gobuster
* Burp Suite
* PHP analysis tools
* Netcat
* Linux enumeration tools

---

# Vulnerabilities Identified

## PHP Object Deserialization

**Type:** Remote Code Execution

**Impact:**

Unsafe deserialization can allow attackers to manipulate application objects and execute unauthorized actions.

---

## Linux Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

Misconfigured permissions can allow users to gain elevated privileges.

---

# Lessons Learned

* Never deserialize untrusted user input.
* Application source code can reveal critical vulnerabilities.
* Web vulnerabilities should always be followed by privilege escalation checks.
* Secure coding practices are essential for preventing remote code execution.
