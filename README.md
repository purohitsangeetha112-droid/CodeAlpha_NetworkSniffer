# 🛡️ CodeAlpha Network Sniffer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-00D9FF?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Scapy-Packet_Analysis-7C3AED?style=for-the-badge" alt="Scapy">
  <img src="https://img.shields.io/badge/Status-Completed-00C853?style=for-the-badge" alt="Completed">
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-FF1744?style=for-the-badge" alt="Cybersecurity">
</p>

<p align="center">
  <b>Real-Time Network Packet Capture & Analysis</b>
  <br>
  CodeAlpha Cyber Security Internship — Task 1
</p>

---

## 📑 Table of Contents

* [🎯 Project Overview](#-project-overview)
* [✨ Features](#-features)
* [🧰 Technologies Used](#-technologies-used)
* [⚙️ Prerequisites](#️-prerequisites)
* [🚀 Installation](#-installation)
* [▶️ Usage](#️-usage)
* [📸 Sample Output](#-sample-output)
* [📚 Learning Outcomes](#-learning-outcomes)
* [⚠️ Disclaimer](#️-disclaimer)
* [👩‍💻 Author](#-author)

---

## 🎯 Project Overview

**CodeAlpha Network Sniffer** is a Python-based network monitoring tool developed using the **Scapy** library.

It captures live network packets and displays useful information such as:

* Source and destination IP addresses
* Source and destination ports
* Network protocols
* Packet timestamps and sizes
* Available packet payload information

The main objective is to understand how devices communicate over a network and gain practical experience with packet capture and network traffic analysis.

> **MISSION:** Capture. Inspect. Understand. Secure.

---

## ✨ Features

| Feature                    | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| 📡 Live Capture            | Captures packets from an available network interface      |
| 🌐 Protocol Identification | Identifies supported protocols such as TCP, UDP, and ICMP |
| 🔌 Port Information        | Displays source and destination ports when available      |
| 📦 Packet Inspection       | Examines packet metadata and available payload data       |
| ⏱️ Timestamps              | Displays packet capture time and packet size              |
| 🖥️ Formatted Output       | Presents packet information in a readable console format  |

---

## 🧰 Technologies Used

* **Python 3** — Main programming language
* **Scapy** — Packet capture and inspection
* **Npcap** — Packet capture support on Windows
* **TCP/IP** — Network communication fundamentals
* **Git & GitHub** — Version control and project hosting

---

## ⚙️ Prerequisites

Before running this project, make sure you have:

* Python 3.8 or later
* Git installed
* Required Python dependencies
* Npcap installed on Windows, if needed
* Appropriate administrator or root privileges

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/purohitsangeetha112-droid/CodeAlpha_NetworkSniffer.git
```

### 2. Navigate to the Project Folder

```bash
cd CodeAlpha_NetworkSniffer
```

If the Python files are inside the `packet sniffer` folder, navigate into it:

```bash
cd "packet sniffer"
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Windows Setup

Install Npcap if it is required for your environment.

Official website: https://npcap.com/

Follow the installation instructions for your system.

---

## ▶️ Usage

Network packet capture may require elevated privileges.

### Windows

Open PowerShell or your terminal as Administrator and run:

```bash
python network_sniffer.py
```

### Linux

Run the script with the necessary permissions:

```bash
sudo python3 network_sniffer.py
```

### Generate Traffic

Once the sniffer is running, open a browser or perform normal network activity on your own device.

The program will display packets that it successfully captures from the selected interface.

**Note:** The exact output depends on your network interface and the implementation of your script.

---

## 📸 Sample Output

The following is an illustrative example of the expected output format.

```text
🚀 Starting Advanced Network Sniffer...
⏳ Waiting for packets...

=======================================================
📦 PACKET #1 | ⏰ Time: 19:09:31 | 📏 Size: 119 bytes
-------------------------------------------------------
🌐 Source IP       : 192.168.1.6
🎯 Destination IP  : 224.0.0.251
📡 Protocol        : UDP (Code: 17)
🔌 Source Port     : 5353
🔌 Destination Port: 5353
📝 Payload (Data)  : [No Data]
=======================================================
```

*Sample output is illustrative. Actual packet information may differ.*

---

## 📚 Learning Outcomes

This project provides practical exposure to:

* Network packet capture and analysis
* IP addressing and network communication
* TCP, UDP, and ICMP protocols
* Source and destination port identification
* Packet metadata and payload inspection
* Using Python and Scapy for network analysis
* Basic cybersecurity monitoring concepts

---

## ⚠️ Disclaimer

This project was developed for **educational purposes** as part of the CodeAlpha Cyber Security Internship.

* Monitor only networks and devices you own or have explicit permission to monitor.
* Respect user privacy and applicable laws.
* Do not use this tool to intercept private communications without authorization.

**Use this tool responsibly and only for authorized security testing.**

---

## 👩‍💻 Author

**Sangeetha kumari B**

Cybersecurity Student | Aspiring Cybersecurity Professional

**Internship:** CodeAlpha Cyber Security Internship
**Project:** Task 1 — Network Sniffer

---

<p align="center">
  <b>🛡️ Learn Networks. Analyze Packets. Strengthen Security.</b>
</p>
