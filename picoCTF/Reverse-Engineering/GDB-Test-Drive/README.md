# picoCTF - GDB Test Drive

## Challenge Information

| Field      | Details                         |
| ---------- | ------------------------------- |
| Platform   | picoCTF                         |
| Category   | Reverse Engineering             |
| Difficulty | Easy                            |
| Skills     | GDB, Debugging, Binary Analysis |

---

# Overview

GDB Test Drive is a reverse engineering challenge focused on learning the basics of debugging with GDB.

The challenge introduces how security researchers analyze executable programs by inspecting memory, registers, and program execution flow.

The attack path includes:

* Loading the binary into GDB
* Inspecting program behavior
* Examining variables and memory
* Recovering the required information

---

# Reconnaissance

The provided binary was analyzed.

The file type was identified:

```bash id="6q5w9a"
file debugger0_a
```

The executable was loaded into GDB:

```bash id="8n3r2x"
gdb debugger0_a
```

---

# Debugging Analysis

GDB was used to inspect the binary during execution.

Useful commands:

```bash id="2v7p8m"
info functions
```

Lists available functions.

```bash id="4m8x1q"
break main
```

Creates a breakpoint.

```bash id="5z2k9v"
run
```

Starts program execution.

---

# Solution

The program was executed under the debugger and examined step by step.

The analysis focused on:

* Program flow
* Memory contents
* Register values
* Important variables

The required value was identified through debugging.

---

# Flag Retrieval

After locating the relevant information using GDB, the challenge flag was recovered.

---

# Tools Used

* GDB
* Linux terminal
* Binary analysis tools

---

# Skills Demonstrated

## Debugging

Using a debugger to inspect and control program execution.

## Binary Analysis

Understanding executable behavior at a low level.

## Reverse Engineering

Analyzing compiled programs to recover information.

---

# Technical Concepts

## GNU Debugger (GDB)

GDB is a debugging tool used for:

* Setting breakpoints
* Inspecting memory
* Viewing registers
* Stepping through execution

## Dynamic Analysis

Dynamic analysis examines software while it is running to understand its behavior.
