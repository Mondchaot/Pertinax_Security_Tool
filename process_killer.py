
# process_killer.py – Beendet gefährliche Prozesse anhand von Signaturen
import psutil
import os
import time
import platform

# Verdächtige Prozessnamen oder Hashes (erweiterbar)
BLACKLISTED_PROCESSES = ["keylogger.exe", "stealer.py", "malware_service", "cryptominer"]

def is_malicious(proc):
    try:
        name = proc.name().lower()
        for bad in BLACKLISTED_PROCESSES:
            if bad in name:
                return True
    except:
        pass
    return False

def kill_process(proc):
    try:
        proc.kill()
        print(f"[🛑] Prozess beendet: {proc.name()} (PID {proc.pid})")
    except Exception as e:
        print(f"[!] Fehler beim Beenden: {proc.name()} – {e}")

def monitor_processes():
    print("[🔎] Starte Prozessüberwachung...")
    while True:
        for proc in psutil.process_iter():
            if is_malicious(proc):
                kill_process(proc)
        time.sleep(20)

if __name__ == "__main__":
    monitor_processes()
