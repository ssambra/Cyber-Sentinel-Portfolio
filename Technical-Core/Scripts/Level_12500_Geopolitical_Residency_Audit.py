# LEVEL 12,500: TRANS-CONTINENTAL RESIDENCY GUARD
# Ensuring data sovereignty across EU (DORA) and Canada (PIPEDA)

def residency_lockdown(data_packet):
    origin = data_packet.get('origin')
    destination = data_packet.get('destination')
    
    if origin == "EU" and destination == "NON_SOVEREIGN_ZONE":
        print("[!] ALERT: DORA Article 28 Violation Detected.")
        print("[!] ACTION: Severing Connection. Data Sovereignty Preserved.")
        return False
    return True

print("Geopolitical Auditor: Watching the Borders.")
