# picoCTF - PW Crack 5

## Challenge Information

| Field      | Details                                                 |
| ---------- | ------------------------------------------------------- |
| Platform   | picoCTF                                                 |
| Category   | General Skills                                          |
| Difficulty | Medium                                                  |
| Skills     | Python Scripting, Automation, Reverse Engineering Logic |

---

# Overview

PW Crack 5 is a challenge focused on analyzing a password-checking program and creating a script to automatically determine the correct password.

Instead of manually testing possible passwords, the challenge requires understanding the program logic and automating the process.

The attack path includes:

* Reviewing Python source code
* Understanding password validation logic
* Automating password attempts
* Retrieving the flag

---

# Reconnaissance

The challenge provides a Python script responsible for checking a password.

The source code was inspected:

```bash
cat level5.py
```

The script contained:

* A password verification function
* A list of possible password values
* Logic comparing user input against the correct password

---

# Source Code Analysis

The program contained multiple possible password values.

Instead of manually entering each value, the process could be automated.

The important part of the script was identifying how the password was checked.

Example logic:

```python
if user_input == correct_password:
    print(flag)
```

The goal was to determine the valid input automatically.

---

# Exploitation

A Python script was created to test the available password candidates.

Example:

```python
for password in passwords:
    test(password)
```

The script automated the guessing process and identified the correct password.

After entering the valid password, the challenge returned the flag.

---

# Solution Approach

The main technique was not brute force against a remote service, but analyzing the application logic and writing automation to solve the challenge efficiently.

This demonstrates how scripting can reduce repetitive security testing tasks.

---

# Tools Used

* Python
* Linux command line
* Source code analysis

---

# Skills Demonstrated

## Python Automation

Using scripts to automate repetitive tasks.

## Code Analysis

Understanding how a program processes input and validates data.

## Problem Solving

Finding the fastest approach instead of manually testing possibilities.

---

# Lessons Learned

* Source code review can reveal weaknesses in application logic.
* Automation is an important skill in security testing.
* Small scripts can save significant time during assessments.
* Understanding program behavior is often more effective than guessing inputs manually.
