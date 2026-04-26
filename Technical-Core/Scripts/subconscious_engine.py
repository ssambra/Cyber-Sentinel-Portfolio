import time, random
def silicon_dream():
    scenarios = ["Warsaw Analyst", "Madrid Auditor", "Berlin Intelligence"]
    print("[!] SUBCONSCIOUS ACTIVE: Simulating paths...")
    for i in range(3):
        time.sleep(1)
        sim = f"Path: {random.choice(scenarios)} | Logic: Verified"
        print(f"[-] {sim}")
        with open("/Users/melissa.wozney/Sentinel-Core/Intelligence/subconscious.log", "a") as log:
            log.write(f"{time.ctime()}: {sim}\n")
    print("[!] SIMULATION COMPLETE.")
if __name__ == "__main__":
    silicon_dream()
