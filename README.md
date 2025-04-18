# 🛰️ Network Congestion Control Evaluation with Pantheon

This repository contains all files related to the evaluation and comparison of different congestion control protocols using the Pantheon framework and Mahimahi. The project investigates how CUBIC, BBR, and Copa perform in terms of **Round Trip Time (RTT)**, **Throughput**, and **Packet Loss** under a consistent network profile.

---

## 📌 Overview

The objective of this assignment is to analyze the behavior of three congestion control protocols under a controlled environment:
- **CUBIC**
- **BBR**
- **Copa**

We use a simulated 50 Mbps bandwidth and 10 ms latency profile to observe how each protocol behaves over time. The analysis is supported by:
- Performance metric plots (RTT, throughput, loss)
- Scatter plots for visual correlation
- A detailed written report

---

## 🗂️ Repository Structure

. ├── README.md ├── SaiRamyaValleruN_PA3_Report_CleanTitle.pdf ├── *.png ├── *.txt ├── *.py ├── setup_system.py ├── setup.py ├── plot_profiles.py ├── test.py ├── pantheon_logs/


---

## ⚙️ Setup & Dependencies

**System Requirements:**
- Ubuntu/Linux OS
- Python 2.7.18
- Pantheon
- Mahimahi

**Python packages:**
```bash
pip install matplotlib numpy
🚀 Reproducing the Results

    Clone the repository:

git clone https://github.com/SaiRamyaValleruN/pantheon-pa3-report.git
cd pantheon-pa3-report

    Install dependencies (Pantheon, Mahimahi, etc.)

    Run experiments:

python setup_system.py
sudo python setup.py

    Generate plots:

python plot_profiles.py

📈 Plots Included

    bbr_rtt_plot.png

    cubic_rtt_plot.png

    copa_rtt_plot.png

    throughput_profile1.png

    loss_profile1.png

    perf_scatter.png

    rtt_profile1.png

All plots are labeled with titles, axes, and legends to support comparative analysis.
📝 Report Summary

The report SaiRamyaValleruN_PA3_Report_CleanTitle.pdf includes:

    Full performance evaluation

    Graphs and analysis

    Answers to reflection questions

🤔 Reflections

Reflections on what was challenging, how LLMs were used, and peer interactions are included in the final report.
