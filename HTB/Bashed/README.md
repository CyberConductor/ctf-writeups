# Hack The Box - Bashed

## Machine Information

| Field            | Details                                                                       |
| ---------------- | ----------------------------------------------------------------------------- |
| Platform         | Hack The Box                                                                  |
| Machine          | Bashed                                                                        |
| Difficulty       | Easy                                                                          |
| Operating System | Linux                                                                         |
| Category         | Web Exploitation, Privilege Escalation                                        |
| Main Skills      | Web enumeration, exposed files, command execution, Linux privilege escalation |

---

# Overview

Bashed is a Linux-based machine that demonstrates the risks of exposing development files and misconfigured permissions.

The attack path includes:

* Web reconnaissance
* Discovering an exposed web shell
* Obtaining initial access
* Enumerating Linux permissions
* Exploiting sudo misconfiguration

---

# Reconnaissance

The first step was identifying available services.

## Nmap Scan

```bash id="5tr2ka"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="3p9x4m"
80/tcp HTTP
```

The web server was investigated.

---

# Web Enumeration

Directory enumeration was performed:

```bash id="8q6md1"
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

A suspicious directory was discovered:

```text id="9v2c7x"
/dev/
```

Inside the directory, an exposed web shell was found.

---

# Web Shell Analysis

The discovered page was identified as:

```text id="1k6s8p"
phpbash
```

The application provided command execution through the web interface.

Commands could be executed directly on the target server.

---

# Initial Access

A reverse shell was generated and executed through the web shell.

Listener:

```bash id="6n5w2q"
nc -lvnp 4444
```

A shell connection was received.

The shell was upgraded:

```bash id="8x3m5v"
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

---

# User Enumeration

The current user was identified:

```bash id="7p4k9m"
whoami
```

System information was collected:

```bash id="4c8z2s"
uname -a
```

The user flag was located:

```text id="9m5v1q"
/home/<user>/user.txt
```

---

# Privilege Escalation

Privilege escalation enumeration was performed.

Sudo permissions were checked:

```bash id="3z7m8x"
sudo -l
```

The output revealed that the current user could execute commands with elevated privileges.

---

# Root Access

The sudo permission was abused to execute commands as root.

After escalation:

```bash id="5q8n3c"
whoami
```

Output:

```text id="2m9x7a"
root
```

The root flag was retrieved:

```text id="6v4p8s"
/root/root.txt
```

---

# Tools Used

* Nmap
* Gobuster
* Netcat
* Linux enumeration tools

---

# Vulnerabilities Identified

## Exposed Web Shell

**Type:** Remote Command Execution

**Impact:**

Publicly accessible web shells allow attackers to execute commands on the server.

---

## Sudo Misconfiguration

**Type:** Local Privilege Escalation

**Impact:**

Incorrect sudo permissions allow normal users to gain root privileges.

---

# Lessons Learned

* Development files should never be exposed in production environments.
* Web shells can lead to complete server compromise.
* Always perform privilege escalation enumeration after gaining access.
* Proper file permissions are critical for Linux security.
