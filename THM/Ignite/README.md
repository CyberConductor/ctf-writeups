# TryHackMe - Ignite

## Machine Information

| Field            | Details                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------ |
| Platform         | TryHackMe                                                                                  |
| Machine          | Ignite                                                                                     |
| Difficulty       | Easy                                                                                       |
| Operating System | Linux                                                                                      |
| Category         | Web Exploitation, CMS Enumeration, Privilege Escalation                                    |
| Main Skills      | CMS exploitation, credential discovery, configuration analysis, Linux privilege escalation |

---

# Overview

Ignite is a Linux-based challenge focused on exploiting a vulnerable Fuel CMS installation.

The attack path includes:

* Web enumeration
* CMS identification
* Exploiting a known vulnerability
* Obtaining remote access
* Privilege escalation through insecure configuration

---

# Reconnaissance

The first step was identifying available services.

## Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text
80/tcp HTTP
```

The web service was investigated.

---

# Web Enumeration

The website revealed a Fuel CMS installation.

Further enumeration was performed to identify:

* CMS version
* Available endpoints
* Default configuration files

Directory enumeration:

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

---

# Vulnerability Discovery

The CMS version was identified as vulnerable to a known remote code execution vulnerability.

The vulnerability allowed commands to be executed through the affected Fuel CMS component.

---

# Initial Access

A command execution payload was sent through the vulnerable functionality.

A listener was started:

```bash
nc -lvnp 4444
```

A reverse shell connection was received.

The shell was upgraded:

```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

---

# User Enumeration

System information was collected:

```bash
whoami
```

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

The sudo configuration was checked:

```bash
sudo -l
```

A misconfiguration allowed commands to be executed with elevated privileges.

---

# Root Access

The privilege escalation method was used to obtain root access.

Verification:

```bash
whoami
```

Output:

```text
root
```

The root flag was retrieved:

```text
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* Burp Suite
* Netcat
* Linux enumeration tools

---

# Vulnerabilities Identified

## Fuel CMS Remote Code Execution

**Type:** Remote Code Execution

**Impact:**

An attacker can execute arbitrary commands on the server through a vulnerable CMS component.

---

## Privilege Escalation Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect permissions allowed escalation from a normal user to root.
