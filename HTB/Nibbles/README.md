# Hack The Box - Nibbles

## Machine Information

| Field            | Details                                                                           |
| ---------------- | --------------------------------------------------------------------------------- |
| Platform         | Hack The Box                                                                      |
| Machine          | Nibbles                                                                           |
| Difficulty       | Easy                                                                              |
| Operating System | Linux                                                                             |
| Category         | Web Exploitation, Privilege Escalation                                            |
| Main Skills      | Web enumeration, CMS exploitation, file upload bypass, Linux privilege escalation |

---

# Overview

Nibbles is a Linux machine that demonstrates how small configuration mistakes in web applications can lead to full system compromise.

The attack path includes:

* Web enumeration
* Discovering a vulnerable CMS
* Exploiting a file upload vulnerability
* Obtaining a reverse shell
* Escalating privileges through sudo misconfiguration

---

# Reconnaissance

The first step was identifying available services.

## Nmap Scan

```bash id="5n2vkd"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="3v7f1k"
22/tcp SSH
80/tcp HTTP
```

The web service was investigated.

---

# Web Enumeration

The website was inspected for hidden directories.

Directory enumeration:

```bash id="j8m4rs"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

A hidden directory was discovered:

```text id="9h2w7p"
/nibbleblog/
```

The application was identified as:

```text id="4k9x2a"
Nibbleblog CMS
```

---

# CMS Enumeration

The CMS version was identified through the website files.

The installed version was vulnerable.

Further research revealed a known exploit affecting the CMS.

---

# Exploitation

The vulnerability allowed authenticated users to upload malicious files through the plugin upload functionality.

A PHP payload was prepared and uploaded.

The uploaded file provided command execution on the server.

A listener was started:

```bash id="1n4c7p"
nc -lvnp 4444
```

After triggering the uploaded file, a reverse shell was received.

---

# Initial Access

The shell was stabilized:

```bash id="6p9m3x"
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

The current user was identified:

```bash id="0m8q5d"
whoami
```

---

# User Flag

The user flag was found inside the user's home directory:

```text id="7r2m8n"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Sudo permissions were checked:

```bash id="2k6v9s"
sudo -l
```

The output revealed that the current user could execute a specific command with elevated privileges.

---

# Root Access

The sudo configuration was abused to execute commands as root.

After escalation:

```bash id="q5x8mw"
whoami
```

Output:

```text id="5z1c9p"
root
```

The root flag was retrieved:

```text id="9f4m2k"
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* Browser Developer Tools
* Netcat
* Linux enumeration tools

---

# Vulnerabilities Identified

## Vulnerable CMS Plugin Upload

**Type:** Remote Code Execution

**Impact:**

An attacker with valid access can upload malicious files and execute commands on the server.

---

## Sudo Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect sudo permissions can allow users to execute privileged commands.

---

# Lessons Learned

* CMS version identification is important during web assessments.
* File upload functionality requires strict validation.
* Authentication does not always prevent exploitation.
* Always check sudo permissions after gaining user access.
