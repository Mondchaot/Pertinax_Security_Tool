
# registry_watch.py – Überwacht sicherheitsrelevante Registry-Schlüssel unter Windows
import winreg
import time

WATCH_KEYS = [
    r"SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
    r"SYSTEM\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile"
]

def read_registry_values(key_path):
    values = {}
    try:
        hive = winreg.HKEY_LOCAL_MACHINE if key_path.startswith("SYSTEM") else winreg.HKEY_CURRENT_USER
        reg_key = winreg.OpenKey(hive, key_path, 0, winreg.KEY_READ)
        for i in range(0, winreg.QueryInfoKey(reg_key)[1]):
            name, value, _ = winreg.EnumValue(reg_key, i)
            values[name] = value
        winreg.CloseKey(reg_key)
    except Exception as e:
        values["__ERROR__"] = str(e)
    return values

def monitor_registry():
    print("[🔍] Überwache Registry-Einträge auf Veränderungen...")
    snapshots = {key: read_registry_values(key) for key in WATCH_KEYS}

    while True:
        for key in WATCH_KEYS:
            current = read_registry_values(key)
            if current != snapshots[key]:
                print(f"[⚠] Veränderung erkannt in Registry: {key}")
                print("Alt:", snapshots[key])
                print("Neu:", current)
                snapshots[key] = current
        time.sleep(30)

if __name__ == "__main__":
    monitor_registry()
