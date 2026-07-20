# TryHackMe - GLITCH

## Machine Information

| Field            | Details                                                                          |
| ---------------- | -------------------------------------------------------------------------------- |
| Platform         | TryHackMe                                                                        |
| Machine          | GLITCH                                                                           |
| Difficulty       | Easy                                                                             |
| Operating System | Linux                                                                            |
| Category         | Web Exploitation, Enumeration, Privilege Escalation                              |
| Main Skills      | API analysis, web exploitation, credential discovery, Linux privilege escalation |

---

# Overview

GLITCH is a Linux-based challenge that focuses on identifying weaknesses in a web application and using discovered information to gain access to the underlying system.

The attack path includes:

* Web reconnaissance
* API and endpoint analysis
* Finding exposed information
* Obtaining initial access
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash id="0k4j5d"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="x5r8pv"
22/tcp SSH
80/tcp HTTP
```

The HTTP service was investigated.

---

# Web Enumeration

Directory enumeration was performed to discover hidden files and endpoints.

Using Gobuster:

```bash id="6x9m2k"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

The enumeration revealed additional web resources.

The application behavior was analyzed to understand available functionality.

---

# Application Analysis

The web application contained endpoints that exposed useful information.

Requests and responses were inspected using browser developer tools and intercepting proxies.

The analysis revealed:

* Hidden API functionality
* Application parameters
* Sensitive information exposure

---

# Initial Access

The discovered information was used to obtain valid access to the system.

A shell was established on the target machine.

Basic enumeration:

```bash id="y2m7qz"
whoami
```

```bash id="j8c4wr"
hostname
```

---

# User Enumeration

After gaining access, files were searched for credentials and useful information.

Example:

```bash id="5g1x8v"
find / -name "*.txt" 2>/dev/null
```

User-related information was discovered.

The user flag was located:

```text id="8q3m7p"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Sudo permissions were checked:

```bash id="4k9n6s"
sudo -l
```

Additional checks:

```bash id="r7m2ax"
find / -perm -u=s -type f 2>/dev/null
```

A weakness in the system configuration was identified.

---

# Root Access

The discovered privilege escalation method allowed commands to be executed with elevated permissions.

After successful escalation:

```bash id="z3p8vw"
whoami
```

Output:

```text id="1n6q4x"
root
```

The root flag was retrieved.

---

# Tools Used

* Nmap
* Gobuster
* Burp Suite
* Browser Developer Tools
* SSH
* Linux enumeration tools

---

# Vulnerabilities Identified

## Web Application Information Disclosure

**Type:** Information Disclosure

**Impact:**

Improper handling of application responses exposed information useful for attackers.

---

## Privilege Escalation Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect permissions allowed a user with limited access to gain higher privileges.
