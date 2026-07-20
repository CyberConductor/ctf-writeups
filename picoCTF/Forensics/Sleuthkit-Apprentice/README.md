# picoCTF - Sleuthkit Apprentice

## Challenge Information

| Field      | Details                                             |
| ---------- | --------------------------------------------------- |
| Platform   | picoCTF                                             |
| Category   | Forensics                                           |
| Difficulty | Easy                                                |
| Skills     | File System Analysis, Sleuth Kit, Digital Forensics |

---

# Overview

Sleuthkit Apprentice is a digital forensics challenge focused on using The Sleuth Kit tools to analyze a disk image.

The challenge introduces basic forensic investigation techniques used to examine filesystems and recover information from storage media.

The attack path includes:

* Inspecting a disk image
* Identifying filesystem information
* Using Sleuth Kit utilities
* Recovering the flag

---

# Reconnaissance

The challenge provides a disk image file.

The first step was identifying the image format:

```bash id="p2i9gd"
file disk.img
```

The image was then analyzed using Sleuth Kit tools.

---

# Filesystem Analysis

The filesystem information was extracted using:

```bash id="h2v4cx"
fsstat disk.img
```

This provided information about:

* Filesystem type
* Block size
* Metadata structures
* Inode information

---

# File Enumeration

The files contained inside the image were listed using:

```bash id="k7d8pu"
fls disk.img
```

The output displayed files and directories stored inside the filesystem.

The relevant file was identified through the file listing.

---

# File Extraction

After locating the target file, its contents were extracted using:

```bash id="w8k3mc"
icat disk.img <inode>
```

The inode number from the file listing was used to recover the file contents.

---

# Flag Retrieval

The extracted file contained the challenge flag.

---

# Tools Used

* The Sleuth Kit
* fsstat
* fls
* icat
* Linux terminal

---

# Skills Demonstrated

## Digital Forensics

Investigating storage images for evidence.

## File System Understanding

Working with metadata, inodes, and filesystem structures.

## Evidence Recovery

Extracting files from forensic images.

---

# Forensic Concepts

## The Sleuth Kit

The Sleuth Kit is a collection of command-line tools used for forensic analysis of disk images.

Common tools:

| Tool   | Purpose                     |
| ------ | --------------------------- |
| fsstat | Shows filesystem details    |
| fls    | Lists files and directories |
| icat   | Extracts file contents      |

---

# Mitigation

To protect systems against forensic data exposure:

* Encrypt storage devices
* Use secure deletion methods
* Protect physical access
* Maintain proper access controls

---

# Lessons Learned

* Disk images can reveal important evidence.
* Metadata provides valuable investigation information.
* Understanding filesystems is essential for forensic analysis.
* Sleuth Kit is a powerful tool for digital investigations.
