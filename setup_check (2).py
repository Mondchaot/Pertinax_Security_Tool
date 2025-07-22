import os
import importlib.util
import platform
import datetime
import sys

REQUIRED_MODULES = {
    "tkinter": "GUI",
    "psutil": "Systemüberwachung",
    "sklearn": "KI-Analyse",
    "Crypto": "Verschlüsselung",
    "socket": "Netzwerkkommunikation"
}

DUMMY_FILES = [
    "firmware_update.bin",
    "secure_capture.cap"
]

DIRECTORIES = [
    "modules", "bin", "logs"
]

LOGFILE = "logs/setup_log.txt"

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOGFILE, "a") as logf:
        logf.write(line + "\n")

def check_python_modules():
    missing = []
    for mod, use in REQUIRED_MODULES.items():
        if not importlib.util.find_spec(mod):
            missing.append((mod, use))
    return missing

def ensure_directories_and_files():
    created = []
    for d in DIRECTORIES:
        if not os.path.exists(d):
            os.makedirs(d)
            created.append(f"Ordner erstellt: {d}")
    for f in DUMMY_FILES:
        path = os.path.join("bin", f)
        if not os.path.exists(path):
            with open(path, "wb") as dummy:
                dummy.write(os.urandom(128))
            created.append(f"Dummy-Datei erstellt: {path}")
    return created

def check_system_drivers():
    drivers = {
        "Linux": ["/dev/sda", "/dev/video0", "/dev/input/event0"],
        "Windows": ["usb.sys", "pci.sys", "acpi.sys"],
        "Darwin": ["/System/Library/Extensions/AppleUSB.kext"]
    }
    current = platform.system()
    found = []
    for driver in drivers.get(current, []):
        exists = os.path.exists(driver) if driver.startswith("/") else True
        found.append(f"{driver} → {'✅' if exists else '❌ FEHLT'}")
    return found

def describe_project_structure(base="."):
    structure = []
    for root, dirs, files in os.walk(base):
        for f in files:
            rel_path = os.path.relpath(os.path.join(root, f), base)
            structure.append(rel_path)
    return structure

def run_full_diagnosis():
    log("🧪 Setup-Diagnose gestartet")

    log("📦 Bibliothekenprüfung:")
    missing = check_python_modules()
    if not missing:
        log("Alle benötigten Bibliotheken sind installiert.")
    else:
        for mod, use in missing:
            log(f"❌ Modul fehlt: {mod} (verwendet für: {use}) – bitte installieren mit: pip install {mod.lower()}")

    log("📁 Strukturprüfung:")
    for msg in ensure_directories_and_files():
        log(msg)

    log("🖥️ Treiberprüfung:")
    for msg in check_system_drivers():
        log(msg)

    log("📂 Projektstruktur:")
    for path in describe_project_structure():
        log(path)

    log("✅ Setup-Diagnose abgeschlossen")

if __name__ == "__main__":
    if not os.path.exists("logs"):
        os.makedirs("logs")
    run_full_diagnosis()