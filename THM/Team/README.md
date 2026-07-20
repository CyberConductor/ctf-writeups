# TryHackMe - Team

## Machine Information

| Field            | Details                                                         |
| ---------------- | --------------------------------------------------------------- |
| Platform         | TryHackMe                                                       |
| Machine          | Team                                                            |
| Difficulty       | Easy                                                            |
| Operating System | Linux                                                           |
| Category         | Web Enumeration, SSH, Privilege Escalation                      |
| Main Skills      | Subdomain enumeration, SSH analysis, Linux privilege escalation |

---

# Overview

Team is a Linux-based challenge focused on discovering hidden web resources, identifying exposed services, and escalating privileges after obtaining initial access.

The attack path includes:

* Network reconnaissance
* Web enumeration
* Subdomain discovery
* SSH access
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash id="m6w9kp"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="h5j3qw"
22/tcp SSH
80/tcp HTTP
```

The web server was investigated further.

---

# Web Enumeration

Directory enumeration was performed:

```bash id="w8n4df"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Additional web resources were discovered.

The application structure was analyzed to identify hidden functionality.

---

# Subdomain Enumeration

Subdomains were searched using DNS enumeration techniques.

Example:

```bash id="4z8y9c"
gobuster vhost -u http://<TARGET_IP> -w /usr/share/wordlists/subdomains.txt
```

A hidden subdomain was discovered.

The newly discovered web service contained additional information.

---

# Initial Access

The discovered information was used to identify valid credentials.

SSH access was attempted:

```bash id="7c0m8q"
ssh <username>@<TARGET_IP>
```

A user shell was obtained.

---

# User Enumeration

After obtaining access:

```bash id="0v5m1k"
whoami
```

System information was collected:

```bash id="5g8r2p"
uname -a
```

The user flag was located:

```text id="d9w7az"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Checking sudo permissions:

```bash id="m4q9cx"
sudo -l
```

Additional checks:

```bash id="w2s8np"
find / -perm -u=s -type f 2>/dev/null
```

A weakness in the system configuration was identified.

---

# Root Access

The identified misconfiguration was exploited to gain elevated privileges.

Verification:

```bash id="n5k7bd"
whoami
```

Output:

```text id="u7p2xq"
root
```

The root flag was successfully obtained.

---

# Tools Used

* Nmap
* Gobuster
* DNS enumeration tools
* SSH
* Linux enumeration utilities

---

# Vulnerabilities Identified

## Hidden Subdomain Exposure

**Type:** Information Disclosure

**Impact:**

Unlisted services may expose additional attack surfaces.

---

## Weak Access Controls

**Type:** Authentication / Configuration Issue

**Impact:**

Insufficient protection of services can allow unauthorized access.

---

## Linux Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

System misconfigurations can allow privilege elevation.
