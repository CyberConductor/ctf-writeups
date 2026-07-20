# picoCTF - Shark on Wire

## Challenge Information

| Field      | Details                                        |
| ---------- | ---------------------------------------------- |
| Platform   | picoCTF                                        |
| Category   | Other                                          |
| Difficulty | Easy                                           |
| Skills     | Network Analysis, Packet Inspection, Wireshark |

---

# Overview

Shark on Wire is a network analysis challenge focused on examining packet captures and identifying suspicious traffic.

The challenge demonstrates how network analysts inspect captured traffic to locate important information hidden inside communication patterns.

The attack path includes:

* Analyzing a packet capture
* Filtering network traffic
* Identifying relevant packets
* Extracting the flag

---

# Reconnaissance

The challenge provides a packet capture file.

The capture was opened using Wireshark:

```bash id="h8j4sx"
wireshark capture.pcap
```

The goal was to identify unusual communication patterns.

---

# Network Analysis

The packet capture was filtered to reduce unnecessary traffic.

Useful filters:

```text id="v8d3mf"
udp
```

and:

```text id="7f2qca"
ip.addr
```

The packet streams were inspected to identify the communication containing the hidden data.

---

# Solution

The relevant packets were identified by analyzing:

* Source addresses
* Destination addresses
* Packet order
* Payload data

The extracted information from the packets revealed the required flag.

---

# Flag Retrieval

After analyzing the correct network traffic, the hidden flag was recovered from the packet data.

---

# Tools Used

* Wireshark
* Packet filtering
* Linux terminal

---

# Skills Demonstrated

## Network Traffic Analysis

Understanding and investigating captured network communication.

## Packet Inspection

Analyzing individual packets to extract useful information.

## Digital Investigation

Finding relevant evidence from large datasets.

---

# Technical Concepts

## Packet Capture Analysis

Packet captures store recorded network traffic and can be used for:

* Troubleshooting
* Security investigations
* Incident response

## Network Forensics

Network forensics involves collecting and analyzing traffic data to investigate security events.
