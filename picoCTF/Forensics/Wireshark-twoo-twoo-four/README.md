# picoCTF - Wireshark twoo twoo four

## Challenge Information

| Field      | Details                                       |
| ---------- | --------------------------------------------- |
| Platform   | picoCTF                                       |
| Category   | Forensics                                     |
| Difficulty | Easy                                          |
| Skills     | Packet Analysis, Wireshark, Network Forensics |

---

# Overview

Wireshark twoo twoo four is a network forensics challenge focused on analyzing packet capture files.

The challenge demonstrates how security analysts investigate network traffic to identify important information hidden inside communication streams.

The attack path includes:

* Opening a packet capture file
* Filtering network traffic
* Following communication streams
* Extracting hidden data

---

# Reconnaissance

The challenge provides a packet capture file:

```text
capture.pcap
```

The file was opened using Wireshark to analyze the captured network traffic.

```bash
wireshark capture.pcap
```

---

# Packet Analysis

The capture contained multiple network packets from different protocols.

Initial investigation focused on:

* Source and destination addresses
* Communication protocols
* Packet contents
* Suspicious traffic patterns

Useful Wireshark filters:

```text
tcp
```

```text
udp
```

```text
http
```

---

# Investigation

The packets were analyzed to identify the relevant communication.

Wireshark's stream reconstruction feature was used:

```
Right Click Packet
→ Follow
→ TCP Stream
```

Following the stream allowed the transmitted information to be reconstructed.

---

# Flag Retrieval

After filtering the traffic and analyzing the correct communication stream, the hidden flag was extracted from the captured data.

---

# Tools Used

* Wireshark
* Packet filtering
* TCP stream analysis

---

# Skills Demonstrated

## Network Forensics

Analyzing captured traffic to investigate security events.

## Protocol Analysis

Understanding how information is transferred across networks.

## Investigation Techniques

Filtering large amounts of data to identify relevant evidence.

---

# Vulnerability / Concept

## Sensitive Data Exposure Through Network Traffic

Network traffic may contain sensitive information if communication is not properly protected.

Attackers or analysts with access to packet captures may recover information from transmitted data.
