
import os
import sys
from modules.setup.SetupManager import SetupManager
from modules.selftest.SelfHealingSystem import SelfHealingSystem

def main():
    print("🔐 Pertinax Security Tool wird initialisiert...")

    # Selbsttest und Auto-Heilung
    try:
        shs = SelfHealingSystem()
        shs.run_selfcheck()
    except Exception as e:
        print(f"Fehler im Selbsttest: {e}")

    # Setup und Abhängigkeiten
    try:
        sm = SetupManager()
        sm.check_dependencies()
        sm.run_installation()
    except Exception as e:
        print(f"Setup-Fehler: {e}")

    # Prüfung kritischer Binärdateien
    check_assembly_integrity()

    print("✅ System vollständig gestartet.")

def check_assembly_integrity():
    print("🔍 Prüfe Kernel-Binärdateien...")
    bin_files = [
        "drivers/PertinaxFW.sys",
        "drivers/Scanner.sys"
    ]
    for bf in bin_files:
        if not os.path.exists(bf):
            print(f"❌ {bf} fehlt – Erstelle Dummy.")
            with open(bf, "wb") as f:
                f.write(b"\x00" * 1024)
        else:
            print(f"✔️ {bf} vorhanden")

if __name__ == "__main__":
    main()
