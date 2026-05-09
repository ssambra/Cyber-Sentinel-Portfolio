# sentinel_check.py
# 12-line Python check for DORA Art 10 / NIS2 Art 21
# Flags off-hours admin, brute-force, and missing change control

def check_event(e):
    # 1. Off-hours admin — DORA Art 10
    if e.role == 'admin' and e.hour not in range(9, 17):
        return 'off-hours admin'
    # 2. Brute then escalate — NIS2 Art 21
    if e.failed >= 3 and e.success:
        return 'brute-then-escalate'
    # 3. No change control — DORA Art 10
    if e.elevated and not e.ticket_id:
        return 'no-change-control'
    return None
