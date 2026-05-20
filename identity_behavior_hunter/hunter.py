#!/usr/bin/env python3
import csv
import json
import urllib.request
import urllib.error
from datetime import datetime

class IdentityHunter:
    def __init__(self, trusted_city="Kitimat", risk_threshold=5.5):
        self.trusted_city = trusted_city
        self.risk_threshold = risk_threshold
        self.alerts_triggered = 0

    def query_ip_reputation(self, ip_address):
        url = f"http://ip-api.com/json/{ip_address}?fields=status,message,country,city,proxy,hosting"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'IdentityHunter/2.0'})
            with urllib.request.urlopen(req, timeout=5) as response:
                data = json.loads(response.read().decode())
                if data.get('status') == 'success':
                    return data
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError):
            pass
        return None

    def calculate_risk_score(self, row, intel_data):
        score = 0.0
        log_city = row.get('City', 'Unknown').strip()

        if log_city.lower() != self.trusted_city.lower():
            score += 4.0
        if log_city == 'Unknown':
            score += 1.5

        if intel_data:
            if intel_data.get('proxy') is True:
                score += 3.5
            if intel_data.get('hosting') is True:
                score += 2.0

            intel_city = intel_data.get('city', '')
            if log_city and intel_city and log_city.lower() != intel_city.lower():
                score += 1.5

        return min(score, 10.0)

    def audit_linkedin_logins(self, file_path):
        print(f"======================================================================")
        print(f"[#] COMPLIANCE AUDIT START: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"======================================================================\n")
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                reader.fieldnames = [field.strip() for field in reader.fieldnames] if reader.fieldnames else []
                for row in reader:
                    login_date = row.get('Date', 'Unknown').strip()
                    ip_addr = row.get('IP Address', '0.0.0.0').strip()
                    location = row.get('City', 'Unknown').strip()

                    if location.lower() == self.trusted_city.lower():
                        continue

                    intel_data = self.query_ip_reputation(ip_addr) if ip_addr != '0.0.0.0' else None
                    risk_score = self.calculate_risk_score(row, intel_data)

                    if risk_score >= self.risk_threshold:
                        self.alerts_triggered += 1
                        print(f"[!!!] DORA ART 10 INCIDENT ALERT [RISK: {risk_score:.1f}/10.0]")
                        print(f"    Timestamp     : {login_date}")
                        print(f"    Location      : {location}")
                        print(f"    Network Address: {ip_addr}")
                        if intel_data:
                            print(f"    Proxy/VPN Check: {intel_data.get('proxy')}")
                            print(f"    Hosting Node  : {intel_data.get('hosting')}")
                        print("-" * 70)
            print(f"[#] AUDIT COMPLETE. Total High-Risk Indicators Flagged: {self.alerts_triggered}")
        except FileNotFoundError:
            print(f"[X] Error: '{file_path}' not found.")

if __name__ == "__main__":
    hunter = IdentityHunter(trusted_city="Kitimat")
    hunter.audit_linkedin_logins('Logins.csv')
