\# 🛡️ Breach Analyzer

A Python-based toolkit for analyzing breach data, fake login visits, and internal password strength. Designed for cybersecurity awareness, audits, and simulations.

---

## 🔍 Features

### ✅ Fake Website Visitor Tracker
- Counts visits per URL
- Flags IPs scanning fake login pages
- Detects burst attacks (10+ hits/min)
- Simulates IP geolocation (e.g. Russia, China)

### 🔐 Password Strength Analyzer
- Detects weak, reused, or short passwords
- Visualizes top reused credentials

### 📊 Bonus Tools
- Phishing email detector (metadata-based)
- PDF report generator (summary of analysis)

---

## 📁 Files

- `track_fake_visits.py`: Analyze suspicious visits and login traps
- `detect_weak_passwords.py`: Check for password strength issues
- `generate_summary_report.py`: Generate PDF/CSV summary
- `access_logs.csv`: Sample log file (you can modify this)
- `breached_accounts.csv`: Simulated leaked credentials

---

## 🚀 Run It

```bash
python track_fake_visits.py
python detect_weak_passwords.py


Then save it with `CTRL+O`, `Enter`, then `CTRL+X`.

---

### 📤 Push it to GitHub:

```bash
git add README.md
git commit -m "Add project README"
git push origin main

