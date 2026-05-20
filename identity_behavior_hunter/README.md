# Identity Behavior Hunter (DORA Art. 10 / NIS2 Art. 21 Compliance)

An automated identity auditing and behavioral anomaly detection engine designed to monitor external corporate attack surfaces and user account footprints using platform-agnostic security log exports.

## 📋 Compliance & Business Value Alignment

* **DORA Article 10 (ICT-Related Incident Detection):** Implements continuous monitoring capabilities to flag unauthorized access, lateral movement risk, and external identity leaks.
* **NIS2 Article 21 (Risk-Management Measures):** Provides clear administrative and technical evidence of active supply-chain and asset access auditing.

---

## 🚀 The Engineering Evolution: Phase 1 to Phase 2

Real-world Security Operations Centers (SOCs) fail when they rely solely on rigid, rule-based alerts that cause severe analyst fatigue. This project demonstrates the systematic optimization of an identity detection pipeline from a rigid binary filter into a contextual, threat-enriched risk engine.

### 🔹 Phase 1: Rule-Based Deterministic Detection (`hunter_baseline.py`)
* **Objective:** Establish a minimum viable compliance detector.
* **Logic:** Ingests flat raw access logs (`.csv`), normalizes headers, and runs a strict binary comparison against an established geographic home-base (`trusted_city`).
* **Outcome:** Successfully flags 100% of out-of-bounds traffic, but introduces high false-positive rates if a user utilizes a corporate VPN or secure routing.

### 🔹 Phase 2: Dynamic Contextual Risk-Scoring Engine (`hunter.py`)
* **Objective:** Eliminate false positives and automate deep incident triaging.
* **Logic:** Re-engineered the procedural script into a class-based, object-oriented framework. When a geographic anomaly is flagged, the script shifts from binary logic to **Proactive Threat Intelligence Enrichment**:
  1. **Live API Query:** Performs a dependency-free networking handshake to pull live ISP, ASN, and routing flags for the anomalous IP.
  2. **Infrastructure Risk Analysis:** Dynamically tracks if the login originated from known public proxies, Tor exit nodes, or commercial hosting facilities (e.g., automated scraper bots / AWS instances).
  3. **Spoofing Detection:** Cross-verifies the user's reported self-asserted location against true IP geolocation routing, identifying active session spoofing.
* **Outcome:** Calculates a dynamic **Risk Score (0.0 - 10.0)**. Alerts are only escalated to the console if they breach a pre-configured critical threat tolerance threshold, ensuring high-fidelity alerting.

---

## 🛠️ How to Run the Audits

### 1. Run the Phase 1 Baseline Core
```bash
python3 hunter_baseline.py
