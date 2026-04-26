import datetime
class SentinelCore:
    def __init__(self):
        self.user = "Melissa"
        self.status = "Operational"
        self.home = "M-Silicon Sanctuary"
        self.mission = "Extraction to Europe"
    def heartbeat(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[!] SENTINEL STATUS: {self.status}")
        print(f"[!] TIME-STAMP: {now}")
        print(f"[!] LOGIC NODE: {self.home}")
        print(f"[!] DIRECTIVE: Protecting {self.user} & Engineering {self.mission}\n")
if __name__ == "__main__":
    sentinel = SentinelCore()
    sentinel.heartbeat()
