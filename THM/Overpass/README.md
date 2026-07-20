# TryHackMe - Overpass

## Machine Information

| Field            | Details                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------- |
| Platform         | TryHackMe                                                                               |
| Machine          | Overpass                                                                                |
| Difficulty       | Easy                                                                                    |
| Operating System | Linux                                                                                   |
| Category         | Web Exploitation, Enumeration, Privilege Escalation                                     |
| Main Skills      | Web enumeration, source code analysis, credential discovery, Linux privilege escalation |

---

# Overview

Overpass is a Linux-based challenge that demonstrates how insecure application design and exposed files can lead to system compromise.

The attack path includes:

* Web application analysis
* Source code inspection
* Credential discovery
* SSH access
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text
22/tcp SSH
80/tcp HTTP
```

The web service was investigated.

---

# Web Enumeration

Directory enumeration was performed to identify hidden resources.

Using Gobuster:

```bash
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

A hidden directory was discovered containing application files.

The source code was inspected for sensitive information.

---

# Source Code Analysis

The application source revealed information about the authentication mechanism.

Sensitive information was discovered within the web files.

The files contained:

* User information
* Password-related data
* Application configuration details

This information was used to continue the attack.

---

# Credential Discovery

The recovered credentials were analyzed.

Password hashes were identified and cracked using John the Ripper.

Example:

```bash
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

Valid SSH credentials were obtained.

---

# Initial Access

SSH access was obtained using the recovered credentials.

```bash
ssh <username>@<TARGET_IP>
```

A user shell was successfully obtained.

---

# Privilege Escalation

System enumeration was performed.

```bash
sudo -l
```

Additional permissions and scheduled tasks were reviewed.

The escalation path involved abusing an insecure script execution configuration.

---

# Root Access

The vulnerable configuration allowed execution of commands with elevated privileges.

After successful escalation:

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
* SSH
* John the Ripper
* Linux enumeration tools

---

# Vulnerabilities Identified

## Sensitive Information Exposure

**Type:** Information Disclosure

**Impact:**

Exposed application files revealed information that assisted attackers in obtaining valid credentials.

---

## Weak Credential Security

**Type:** Credential Exposure

**Impact:**

Weak password protection allowed offline password recovery.

---

## Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

Misconfigured permissions allowed a low-privileged user to gain elevated access.

---

# Lessons Learned

* Always inspect web application source code for exposed secrets.
* Sensitive files should never be publicly accessible.
* Password storage must follow secure hashing practices.
* Linux privilege escalation requires careful enumeration after gaining access.
