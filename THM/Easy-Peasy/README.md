# TryHackMe - Easy Peasy

## Machine Information

| Field            | Details                                                                                |
| ---------------- | -------------------------------------------------------------------------------------- |
| Platform         | TryHackMe                                                                              |
| Machine          | Easy Peasy                                                                             |
| Difficulty       | Easy                                                                                   |
| Operating System | Linux                                                                                  |
| Category         | Web Enumeration, Cryptography, Privilege Escalation                                    |
| Main Skills      | Service enumeration, hidden directories, password cracking, Linux privilege escalation |

---

# Overview

Easy Peasy is a beginner-friendly Linux machine focused on combining multiple common penetration testing techniques.

The attack path includes:

* Network reconnaissance
* Web directory enumeration
* Hidden information discovery
* Password cracking
* SSH access
* Linux privilege escalation

---

# Reconnaissance

The first step was identifying services running on the target.

## Nmap Scan

```bash id="a8y4rm"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed multiple exposed services.

Example:

```text id="5s7j2q"
22/tcp SSH
80/tcp HTTP
```

The available services were investigated further.

---

# Web Enumeration

The web server was analyzed for hidden content.

Directory enumeration was performed:

```bash id="k4n7xp"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

Hidden directories and files were discovered.

The discovered pages contained additional information required for further exploitation.

---

# Hidden Information Discovery

The application exposed clues through:

* Hidden files
* Page source
* Web responses

The discovered information was analyzed to identify usernames and credentials.

Source code review:

```bash id="8r2c6m"
curl http://<TARGET_IP>
```

---

# Password Cracking

A password hash was discovered during enumeration.

The hash was prepared for cracking:

```bash id="x5v9az"
john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

The recovered credentials were used for further access.

---

# Initial Access

SSH access was obtained using the discovered credentials.

```bash id="v7m3kx"
ssh <username>@<TARGET_IP>
```

A user shell was successfully obtained.

---

# User Enumeration

After obtaining access, system enumeration was performed.

Current user:

```bash id="m5q8nc"
whoami
```

System information:

```bash id="t3w6px"
uname -a
```

The user flag was located:

```text id="7c5r2m"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation checks were performed.

Sudo permissions:

```bash id="q9m4wd"
sudo -l
```

SUID binaries:

```bash id="k2z7pf"
find / -perm -u=s -type f 2>/dev/null
```

A vulnerable configuration was identified.

---

# Root Access

The identified weakness was exploited to execute commands with elevated privileges.

Verification:

```bash id="p8w3sn"
whoami
```

Output:

```text id="x6r4mq"
root
```

The root flag was retrieved.

---

# Tools Used

* Nmap
* Gobuster
* Curl
* John the Ripper
* SSH
* Linux enumeration tools

---

# Vulnerabilities Identified

## Information Disclosure

**Type:** Web Information Disclosure

**Impact:**

Hidden resources may expose information useful for attackers.

---

## Weak Password Security

**Type:** Credential Exposure

**Impact:**

Weak passwords can be recovered through offline cracking.

---

## Privilege Escalation Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect system permissions can allow unauthorized privilege elevation.

---

# Lessons Learned

* Always perform thorough enumeration before exploitation.
* Web source code may contain useful hidden information.
* Password strength is critical because exposed hashes can be cracked.
* Linux privilege escalation requires systematic checking of permissions and services.
