# Log Hunt

**Platform:** picoCTF  
**Category:** General Skills  
**Difficulty:** Easy


## Description

The server logs leak fragments of a secret flag.
Each fragment appears inside specific log entries and some entries repeat.
The objective is to reconstruct the original flag from these scattered pieces.


## Initial Analysis

Opening `server.log` reveals normal system messages mixed with special entries:

```
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:00:16] WARN Disk space low
[1990-08-09 10:00:33] WARN Disk space low
```

### Observations

* Only lines containing `FLAGPART:` are relevant
* Each matching line leaks a portion of the flag
* The file is chronological, so the correct order is preserved
* The flag terminates with `}`

Because the log contains many irrelevant and repeated lines, manual reconstruction would be inefficient and error prone.


## Approach

I automated the extraction process:

1. Read the log file line by line
2. Detect lines containing `FLAGPART:`
3. Extract the leaked substring
4. Append fragments sequentially
5. Stop when `}` is reached

The implementation is provided in `server_log.py`.

## Why This Works

The application writes the flag progressively into the log.
Since logs are ordered by time, simply parsing sequentially reconstructs the correct flag.
Stopping at `}` prevents collecting duplicate fragments later in the file.