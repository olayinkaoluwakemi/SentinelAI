# SentinelAI Product Case Study

## 1. Product Overview

SentinelAI is an intelligent cybersecurity assistant for IoT systems. It helps teams detect suspicious device behavior, prioritize incidents, and understand risk in plain language.

The product was designed for environments where connected devices are used across logistics, agriculture, healthcare, and enterprise operations.

---

## 2. Problem Statement

IoT systems create large amounts of operational and network data. However, many teams lack a simple way to identify which activity is suspicious, which devices require urgent attention, and how technical anomalies connect to business risk.

Security tools often produce noisy alerts. Operations teams need a product that reduces alert fatigue and helps them focus on the most important threats.

---

## 3. Target User Persona

### Persona: Security Operations Analyst

**Goals**
- Identify suspicious device activity quickly
- Prioritize urgent threats
- Communicate risk to non-technical stakeholders

**Pain Points**
- Too many alerts without clear context
- Difficulty explaining risk to managers
- Limited visibility across distributed IoT devices
- Manual review of logs takes too much time

---

## 4. Product Goals

SentinelAI aims to:

- Reduce time spent reviewing low-value alerts
- Improve prioritization of high-risk events
- Provide explainable anomaly detection
- Support better communication between security, operations, and leadership teams

---

## 5. Core Features

### Anomaly Detection
Uses machine learning to identify unusual device behavior across network and performance metrics.

### Risk Scoring
Classifies events as Low, Medium, or High risk based on failed logins, CPU usage, data transfer, latency, and model-detected anomalies.

### Explainable Alerts
Each event includes a plain-English explanation of why it may be risky.

### Dashboard Filters
Users can filter by location, device type, and risk level.

### Incident Review Queue
A structured table helps analysts review events by priority.

---

## 6. Success Metrics

| Metric | Why It Matters |
|---|---|
| Time to detect high-risk events | Measures speed of threat visibility |
| Percentage of high-risk alerts reviewed | Measures analyst focus |
| False positive review time | Measures alert fatigue |
| User satisfaction with explanations | Measures product clarity |
| Number of resolved incidents | Measures operational usefulness |

---

## 7. MVP Scope

The MVP includes:

- Synthetic IoT security event dataset
- Machine learning anomaly detection
- Risk-level classification
- Dashboard visualizations
- Incident review table
- Plain-English explanations

---

## 8. Product Trade-Offs

### Simplicity vs. Model Complexity
The MVP uses Isolation Forest because it is lightweight, interpretable enough for early testing, and suitable for anomaly detection.

### Synthetic Data vs. Real Data
Synthetic data makes the product easier to demo publicly while avoiding privacy and security risks.

### Dashboard First vs. Full Integration
The first version focuses on visibility and product storytelling before integrating with live IoT platforms or ticketing systems.

---

## 9. Roadmap

### V1: Dashboard MVP
- Build anomaly dashboard
- Add risk scoring
- Add incident explanations

### V2: Analyst Workflow
- Add investigation notes
- Add alert status
- Add exportable reports

### V3: Enterprise Integration
- Connect to cloud IoT platforms
- Add role-based access control
- Integrate with ServiceNow/Jira incident workflows

---

## 10. Interview Story

This project demonstrates my ability to identify a real user problem, define product requirements, build a technical MVP, and connect AI/cybersecurity capabilities to measurable business outcomes.

SentinelAI reflects my background in technical product management, data analytics, IoT systems, and cybersecurity research.