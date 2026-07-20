# picoCTF - Serpentine

## Challenge Information

| Field      | Details                                           |
| ---------- | ------------------------------------------------- |
| Platform   | picoCTF                                           |
| Category   | General Skills                                    |
| Difficulty | Medium                                            |
| Skills     | Python Analysis, Code Reading, Logic Modification |

---

# Overview

Serpentine is a challenge focused on analyzing a Python program and understanding how program flow affects the ability to retrieve the flag.

The challenge demonstrates the importance of reading source code carefully and identifying how functions are called and controlled.

The attack path includes:

* Reviewing Python source code
* Understanding program execution flow
* Identifying hidden functionality
* Modifying execution behavior

---

# Reconnaissance

The challenge provides a Python script.

The source code was inspected:

```bash
cat serpentine.py
```

The program contained multiple functions responsible for different actions.

The code structure was analyzed to understand:

* Available options
* Function calls
* Flag retrieval logic

---

# Source Code Analysis

During analysis, a function responsible for printing the flag was discovered.

Example:

```python
def print_flag():
    # prints flag
```

However, the function was not executed through the normal program flow.

The challenge required understanding how the application handled user input and function execution.

---

# Vulnerability Discovery

The issue was caused by insecure program logic.

The flag functionality existed in the source code, but normal execution did not reach it.

By analyzing the Python code, the correct execution path could be identified.

---

# Exploitation

The program logic was modified to execute the hidden flag function.

The required change allowed the application to reach:

```python
print_flag()
```

After running the modified script:

```bash
python3 serpentine.py
```

the flag was displayed.

---

# Solution Approach

The challenge was solved through source code analysis rather than exploitation of an external service.

The key steps were:

1. Read the Python source.
2. Identify unreachable functionality.
3. Understand program flow.
4. Modify the execution path.

---

# Tools Used

* Python
* Linux terminal
* Text editor

---

# Skills Demonstrated

## Python Code Analysis

Understanding how functions and control flow work.

## Debugging

Identifying why expected functionality is not reached.

## Source Review

Finding hidden behavior inside application code.

---

# Lessons Learned

* Source code can reveal hidden functionality.
* Understanding program flow is important during security assessments.
* Reading code is often the fastest way to solve logic-based challenges.
* Small logic flaws can expose sensitive functionality.
