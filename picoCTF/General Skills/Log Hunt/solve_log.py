#!/usr/bin/env python3

with open("server.log", "r") as file:
    flag = ""
    for line in file:
        if "FLAGPART" in line:
            flag += line.split("FLAGPART: ")[1].strip()
            if flag.endswith("}"):
                break
    print(flag)