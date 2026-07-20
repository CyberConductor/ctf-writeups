# picoCTF - Disk, Disk, Sleuth!

## Challenge Information

| Field      | Details                                    |
| ---------- | ------------------------------------------ |
| Platform   | picoCTF                                    |
| Category   | Forensics                                  |
| Difficulty | Medium                                     |
| Skills     | Disk Analysis, File Systems, Data Recovery |

---

# Overview

Disk, Disk, Sleuth! is a digital forensics challenge focused on analyzing a disk image and recovering hidden information.

The challenge demonstrates how forensic investigators examine storage media, identify partitions, and recover files from disk images.

The attack path includes:

* Analyzing a disk image
* Identifying filesystem structures
* Extracting files
* Recovering hidden data

---

# Reconnaissance

The challenge provides a disk image file.

The first step was identifying the file type:

```bash
file disk.img
```

The output revealed that the file contained a filesystem image that required further analysis.

---

# Disk Image Analysis

The disk image was examined using forensic tools.

The partition structure was analyzed:

```bash
fdisk -l disk.img
```

This revealed information about:

* Partitions
* Filesystem layout
* Disk offsets

---

# Filesystem Investigation

The image was mounted or inspected using forensic utilities.

Tools such as:

```bash
fls
```

and:

```bash
icat
```

were used to examine the filesystem contents.

The goal was to locate deleted, hidden, or unusual files.

---

# Data Recovery

The filesystem contained information that was not immediately visible through normal browsing.

Using forensic analysis techniques, the relevant file was identified and extracted.

Example:

```bash
icat image.dd <inode>
```

The extracted content contained the required information.

---

# Flag Retrieval

After recovering the hidden file from the disk image, the flag was obtained.

---

# Tools Used

* Sleuth Kit
* fdisk
* file
* fls
* icat
* Linux terminal

---

# Skills Demonstrated

## Disk Forensics

Analyzing storage images for evidence.

## File System Analysis

Understanding how files are stored and recovered.

## Data Recovery

Extracting information that is not visible through normal access methods.

---

# Forensic Concepts

## Disk Images

A disk image is a complete copy of storage media, including:

* Files
* Metadata
* Partitions
* Deleted data

## Deleted Data Recovery

Even after deletion, file information may remain recoverable until overwritten.

---

# Mitigation

To protect sensitive data:

* Properly wipe storage before disposal
* Encrypt sensitive drives
* Apply secure deletion policies
* Restrict physical access to storage devices

---

# Lessons Learned

* Disk images contain valuable forensic evidence.
* Deleted files may still be recoverable.
* File system knowledge is important for investigations.
* Tools like Sleuth Kit are widely used in digital forensics.
