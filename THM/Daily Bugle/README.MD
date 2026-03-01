# Daily Bugle

**Platform:** TryHackMe  
**Difficulty:** Hard  
**Focus Areas:** Web exploitation, SQL injection, credential abuse, reverse shell, Linux privilege escalation  


## Overview

This room involved exploiting a vulnerable Joomla CMS instance to gain initial access, extracting credentials through SQL injection, achieving remote code execution through template modification, and escalating privileges using a misconfigured sudo permission.

The challenge required chaining multiple weaknesses rather than relying on a single exploit.


## 1. Enumeration

Initial scanning was performed using:

```bash
nmap -sC -sV <target-ip>
````

The scan revealed:

* HTTP service running
* `robots.txt` exposing disallowed directories
* Evidence of a Joomla installation

Accessing the Joomla manifest file confirmed the CMS version as **3.7.0**.

Identifying the exact version was critical because it allowed targeted vulnerability research.


## 2. Vulnerability Research

Research showed that Joomla 3.7.0 is vulnerable to an SQL injection tracked as:

**CVE-2017-8917**

The vulnerability exists due to improper sanitisation of user input before it is included in database queries.

This allows attackers to manipulate SQL statements and retrieve sensitive data from the backend database.


## 3. Exploitation

A public proof-of-concept exploit was used to extract database content.

The attack allowed dumping:

* Usernames
* Password hashes

The retrieved hash was identified as **bcrypt** based on the `$2y$` prefix.

Because bcrypt is computationally expensive by design, it slows brute-force attacks. However, weak passwords remain vulnerable to cracking using common wordlists.

After cracking the hash, valid CMS credentials were obtained.


## 4. Gaining Remote Code Execution

With administrative access to Joomla, template files could be modified.

By injecting PHP code into a template file, it was possible to execute arbitrary commands on the server.

This resulted in a reverse shell connection back to the attacking machine.

At this stage, a low-privileged shell as the web user was obtained.


## 5. User Access

Exploring the system revealed a local user directory.

The user flag was located in the home directory of the compromised account.


## 6. Privilege Escalation

Checking sudo permissions:

```bash
sudo -l
```

The user was allowed to execute `/usr/bin/yum` as root without a password.

This is dangerous because `yum` supports plugin functionality.

Using documented techniques from GTFOBins, a malicious plugin was created that executed `/bin/sh`.

Running `yum` with the custom plugin configuration resulted in a root shell.
