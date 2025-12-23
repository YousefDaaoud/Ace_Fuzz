<!-- ===================================================== -->
<!--                    🂡 AceFuzz README                  -->
<!-- ===================================================== -->

# 🂡 AceFuzz

<p align="center">
  <img src="assets/acefuzz-banner.gif" width="420" />
</p>

<h4 align="center">
Smart • Fast • Modern Web Fuzzing & Enumeration Framework
</h4>

<p align="center">
  Automated baseline detection • Smart filtering • Zero-noise results
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" />
  <img src="https://img.shields.io/badge/Status-Active-success.svg" />
  <img src="https://img.shields.io/badge/Focus-Web%20Security-red.svg" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" />
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=AceFuzz&label=Project%20Views&color=0e75b6&style=flat" />
  <img src="https://img.shields.io/github/stars/yourusername/AceFuzz?label=Stars" />
  <img src="https://img.shields.io/github/forks/yourusername/AceFuzz?label=Forks" />
</p>

## 🚀 Overview

**AceFuzz** is a high-performance, intelligent web fuzzing & enumeration framework  
written in **Python** and designed for **real-world offensive security workflows**.

Unlike traditional fuzzers, AceFuzz **learns the target first**, filters noise automatically,  
and displays **only real, meaningful findings**.

> Built to minimize false positives and maximize signal.

## 🔥 Why AceFuzz?

✔ No fake-404 noise  
✔ No manual filter flags  
✔ No response-length guessing  
✔ Clean output by default  
✔ Fast and scalable  

AceFuzz thinks **before** reporting.

## ✨ Features

- ⚡ Multi-threaded scanning  
- 🧠 Automatic baseline detection  
- 🎯 Smart auto-filtering (zero flags)  
- 🧬 Similarity-based response analysis  
- 📁 Directory & file fuzzing  
- 🌐 Subdomain enumeration  
- 🖥️ Virtual host (VHost) enumeration  
- ⏱️ Execution time tracking  
- 📤 Automatic output (JSON & TXT)  
- 📊 Scan summary report  
- 🎨 Clean CLI banner & branding  

## 🎥 Live Demo

<p align="center">
  <img src="assets/dir-fuzz.gif" width="300" />
  <img src="assets/subdomain.gif" width="300" />
  <img src="assets/vhost.gif" width="300" />
</p>

## 📦 Installation

git clone https://github.com/yourusername/AceFuzz.git  
cd AceFuzz  
pip install -r requirements.txt  

## ▶️ Usage

📁 Directory & File Fuzzing  
python acefuzz.py dir -u http://example.com -w wordlists/common.txt -t 100  

🌐 Subdomain Enumeration  
python acefuzz.py subdomain -d example.com -w wordlists/subdomains.txt -t 200  

🖥️ VHost Enumeration  
python acefuzz.py vhost -u http://10.10.10.10 -w wordlists/vhosts.txt -t 80  

## 🧠 How AceFuzz Works

1️⃣ Baseline Detection  
Sends requests to random non-existing paths  
Learns custom 404 / fake responses automatically  

2️⃣ Smart Auto-Filtering  
Detects common response patterns  
Removes noise without user configuration  

3️⃣ Similarity Analysis  
Compares responses against baseline content  
Ignores highly similar pages  

4️⃣ Result Validation  
Displays & saves only valid findings  

## 📤 Output & Reports

AceFuzz automatically generates:  
📄 JSON results  
📄 TXT results  

## 🂡 Author

<p align="center">
  <img src="assets/hacker-terminal.gif" width="120" />
</p>

<h3 align="center">Ace_J0H4ck</h3>

<p align="center">
  Offensive Security • Automation • Tooling
</p>

## ⚠️ Legal Notice

<p align="center">
  <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif" width="90" />
</p>

<p align="center">
  <b>Educational & Authorized Use Only</b><br>
  Do NOT use AceFuzz against systems you do not own or have explicit permission to test.
</p>
