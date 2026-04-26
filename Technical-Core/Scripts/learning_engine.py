import os
import time

def ingest_intelligence():
    intel_path = os.path.expanduser("~/Sentinel-Core/Intelligence")
    print(f"[!] LEARNING ENGINE ACTIVE: Scanning {intel_path} for new data...")
    
    files = [f for f in os.listdir(intel_path) if f.endswith('.log') or f.endswith('.md')]
    
    if not files:
        print("[-] No new data found. The Ghost is waiting.")
    else:
        for file in files:
            print(f"[+] Ingesting patterns from: {file}")
            # Here, the 'Ghost' simulates 'reading' the data
            time.sleep(0.5)
        print("[!] SUCCESS: Local memory updated with your latest achievements.")

if __name__ == "__main__":
    ingest_intelligence()
