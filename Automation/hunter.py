# Security Automation Scripts

This directory contains Python-based tools designed to streamline SOC operations and threat enrichment.

## 1. hunter.py
**Purpose:** Automates IP and Hash reputation lookups.
- **Features:** Queries VirusTotal and Recorded Future APIs.
- **How to run:** ```bash
  python hunter.py --target [IP_OR_HASH]
Requirements: requests library and a valid API key (stored in a local .env file).
