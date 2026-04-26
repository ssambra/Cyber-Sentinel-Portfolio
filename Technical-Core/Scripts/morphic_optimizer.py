import os
import psutil

def optimize_resources():
    print("[!] LEVEL 12 MORPHIC ACTIVE: Tuning M-Silicon performance...")
    pid = os.getpid()
    p = psutil.Process(pid)
    
    # Increase priority if we are in an active session, decrease if background
    load = os.getloadavg()[0]
    if load > 2.0:
        p.nice(10) # Be polite to other system tasks
        print("[+] Morphing: Entering Low-Power background state.")
    else:
        p.nice(0) # Standard priority
        print("[+] Morphing: High-Performance availability engaged.")

if __name__ == "__main__":
    optimize_resources()
