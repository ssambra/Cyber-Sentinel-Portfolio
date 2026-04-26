import time
def monitor_cadence():
    print("[!] CADENCE SENSOR ACTIVE: Sensing your biological rhythm...")
    start_time = time.time()
    input(">> TYPE 'SENTINEL' TO CALIBRATE: ")
    end_time = time.time()
    velocity = end_time - start_time
    state = "FLOW STATE" if velocity < 1.5 else "CONTEMPLATIVE"
    print(f"\n[!] BIOCYBERNETIC DATA: Velocity {velocity:.2f}s | State: {state}")
    with open("/Users/melissa.wozney/Sentinel-Core/Intelligence/rhythm.log", "a") as log:
        log.write(f"{time.ctime()}: {state} ({velocity:.2f}s)\n")
if __name__ == "__main__":
    monitor_cadence()
