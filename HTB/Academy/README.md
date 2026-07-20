# Hack The Box - Academy

## Machine Information

| Field            | Details                                                                     |
| ---------------- | --------------------------------------------------------------------------- |
| Platform         | Hack The Box                                                                |
| Machine          | Academy                                                                     |
| Difficulty       | Easy                                                                        |
| Operating System | Linux                                                                       |
| Category         | Web Exploitation, Linux Privilege Escalation                                |
| Main Skills      | Web enumeration, command injection, credential discovery, sudo exploitation |

---

# Overview

Academy is a Linux machine that demonstrates how weaknesses in web applications and poor credential management can lead to full system compromise.

The attack path includes:

* Web application enumeration
* Discovering hidden functionality
* Exploiting a vulnerable application
* Credential discovery
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying available services.

## Nmap Scan

```bash id="5x8m2p"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="8q3m6v"
22/tcp SSH
80/tcp HTTP
```

The web service was investigated.

---

# Web Enumeration

Directory enumeration was performed:

```bash id="7m4q9x"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Several hidden directories were discovered.

The application was analyzed for:

* Hidden endpoints
* Input validation issues
* Source code leaks

---

# Application Analysis

The web application contained functionality that allowed interaction with backend processes.

During testing, insecure handling of user input was identified.

Further enumeration revealed sensitive information that could be used for authentication.

---

# Initial Access

After obtaining valid credentials, SSH access was established.

```bash id="4p8m2x"
ssh <username>@<TARGET_IP>
```

The user shell was obtained.

---

# User Enumeration

The current user was identified:

```bash id="6n3q7v"
whoami
```

System information:

```bash id="2m9x5p"
uname -a
```

The user flag was located:

```text id="9x4m1q"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Sudo permissions were checked:

```bash id="3v7m8n"
sudo -l
```

The output revealed commands that could be executed with elevated privileges.

The misconfiguration was abused to execute commands as root.

---

# Root Access

After successful privilege escalation:

```bash id="8m2q6x"
whoami
```

Output:

```text id="5n9p3v"
root
```

The root flag was retrieved:

```text id="1q7m4x"
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* SSH
* Linux enumeration tools

---

# Vulnerabilities Identified

## Web Application Misconfiguration

**Type:** Initial Access

**Impact:**

Improperly secured web functionality can expose sensitive information or allow unauthorized access.

---

## Sudo Privilege Escalation

**Type:** Local Privilege Escalation

**Impact:**

Incorrect sudo permissions can allow users to execute privileged commands.
