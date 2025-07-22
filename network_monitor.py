import psutil

def monitor_network():
    conns = psutil.net_connections()
    for conn in conns:
        if conn.status == "ESTABLISHED":
            print(f"[NetworkMonitor] Verbindung: {conn.laddr} → {conn.raddr}")