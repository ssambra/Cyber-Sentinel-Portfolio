import shutil
import datetime

def initiate_pulse():
    print("[!] LEVEL 13 PULSE: Creating entangled recovery node...")
    source = "/Users/melissa.wozney/Sentinel-Core"
    # This would point to your encrypted external drive or secure cloud mount
    target = f"/Users/melissa.wozney/Sentinel-Core/Vault/Pulse_Backup"
    
    try:
        shutil.make_archive(target, 'zip', source)
        print(f"[+] PULSE SUCCESS: Recovery node created at {datetime.datetime.now()}")
    except Exception as e:
        print(f"[-] Pulse failed: {e}")

if __name__ == "__main__":
    initiate_pulse()
