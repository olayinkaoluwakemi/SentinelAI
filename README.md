# SentinelAI: Intelligent Cybersecurity Assistant for IoT Systems

SentinelAI is a product + analytics project that detects suspicious behavior in IoT environments and translates technical anomaly signals into clear, actionable insights for decision-makers.

This project was designed as a Technical Product Management portfolio project for internships in Product Management, Technical Program Management, AI systems, cybersecurity, enterprise SaaS, and data analytics.

---

## Problem

IoT systems generate large volumes of device and network activity, but many operations teams struggle to quickly understand which signals indicate real risk. Security alerts are often too technical, noisy, or disconnected from business impact.

For logistics, healthcare, agriculture, and enterprise environments, delayed detection can lead to data exposure, shipment disruption, compliance risk, and operational downtime.

---

## Solution

SentinelAI provides a simple dashboard that:

- Detects anomalous IoT device behavior
- Assigns risk levels to suspicious events
- Explains why an event may be risky
- Helps teams prioritize incidents by severity, device, and location

---

## Target Users

### Primary User
Security analyst or operations manager responsible for monitoring connected devices.

### Secondary Users
Product managers, IT support teams, compliance teams, and executives who need high-level visibility into digital risk.

---

## Core Features

- Anomaly detection using machine learning
- Risk scoring by device activity
- Interactive filtering by location, device type, and severity
- Executive dashboard metrics
- Plain-English explanations for suspicious behavior

---

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Plotly
- Synthetic IoT cybersecurity dataset

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/SentinelAI.git
cd SentinelAI
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
streamlit run app.py
```

---

## Product Metrics

Success can be measured by:

- Reduction in false alert review time
- Increase in high-risk incident prioritization accuracy
- Time to detect suspicious behavior
- Number of anomalies investigated
- Analyst satisfaction with alert explanations

---

## Product Roadmap

### Version 1
- Build dashboard with anomaly detection and risk scoring
- Add filters and executive metrics

### Version 2
- Add natural-language incident summaries
- Add alert history and investigation notes

### Version 3
- Add role-based access
- Integrate with cloud IoT platforms and ticketing systems

---

## Why This Project Matters

This project shows the ability to combine product thinking, user research, data analytics, cybersecurity, and AI into one practical solution. It demonstrates both technical execution and product strategy.