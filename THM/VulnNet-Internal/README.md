# TryHackMe - VulnNet: Internal

## Machine Information

| Field            | Details                                                                      |
| ---------------- | ---------------------------------------------------------------------------- |
| Platform         | TryHackMe                                                                    |
| Machine          | VulnNet: Internal                                                            |
| Difficulty       | Easy                                                                         |
| Operating System | Linux                                                                        |
| Category         | Internal Network, Web Exploitation, Privilege Escalation                     |
| Main Skills      | Enumeration, internal services, web exploitation, Linux privilege escalation |

---

# Overview

VulnNet: Internal is a Linux-based challenge focused on discovering internal services and exploiting weaknesses in a web application.

The machine demonstrates a common penetration testing scenario:

* External reconnaissance
* Discovering hidden internal services
* Exploiting exposed applications
* Obtaining user access
* Escalating privileges

---

# Reconnaissance

The first step was identifying exposed services.

## Nmap Scan

```bash id="f4q2px"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed available services running on the target.

Example:

```text id="3qz8am"
22/tcp SSH
80/tcp HTTP
```

The web service was investigated further.

---

# Web Enumeration

Directory enumeration was performed to identify hidden paths.

Using Gobuster:

```bash id="5h3p0q"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Hidden endpoints and application files were discovered.

---

# Internal Service Discovery

Further enumeration revealed additional services that were not directly exposed externally.

The discovered information allowed access to internal functionality.

Requests were analyzed to understand:

* Available endpoints
* Application behavior
* Authentication mechanisms

---

# Web Exploitation

The web application contained vulnerabilities that allowed interaction with internal resources.

Testing was performed against discovered functionality.

The vulnerability allowed access to restricted information and assisted with gaining initial access.

---

# Initial Access

After exploiting the vulnerable service, access to the target system was obtained.

A shell was established and system enumeration began.

Basic information gathering:

```bash id="k3v7pm"
whoami
```

```bash id="p7s4dc"
uname -a
```

---

# User Enumeration

Files and directories were reviewed to identify user information.

The user flag was located inside the user's home directory.

```text id="7v8x1p"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Checking sudo permissions:

```bash id="m2k5vx"
sudo -l
```

Additional checks were performed:

```bash id="x8n4qy"
find / -perm -u=s -type f 2>/dev/null
```

A privilege escalation path was identified through system misconfiguration.

---

# Root Access

The identified weakness was exploited to execute commands with elevated privileges.

After escalation:

```bash id="t6y9wa"
whoami
```

Output:

```text id="w2j8km"
root
```

The root flag was successfully retrieved.

---

# Tools Used

* Nmap
* Gobuster
* Curl
* SSH
* Linux enumeration tools
* Privilege escalation scripts

---

# Vulnerabilities Identified

## Exposed Internal Functionality

**Type:** Information Disclosure / Access Control Issue

**Impact:**

Internal services or restricted functionality may become accessible through improper configuration.

---

## Linux Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

Misconfigured permissions allowed privilege elevation from a normal user to root.

---

# Lessons Learned

* Internal services should not be exposed without proper access controls.
* Web applications require careful endpoint enumeration.
* Network segmentation is important for protecting internal resources.
* Always enumerate privilege escalation paths after gaining user access.
