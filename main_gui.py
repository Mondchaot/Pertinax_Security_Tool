import tkinter as tk
from styles import apply_styles
from icons import load_icon
from system_info import get_system_info
from performance_tracker import get_performance_metrics
from tracking_sniffer import generate_mock_path
from crypto_utils import sha256
from usb_exploit_defender import monitor_usb
from hardware_driver_check import check_drivers
from ai_analyzer import AIAnalyzer
from forensic_ki import start_forensic_ki, start_tunnel_for_forensics
import subprocess

ai = AIAnalyzer()

def train_ai_with_system_data():
    metrics = get_performance_metrics()
    values = [metrics["cpu_usage_percent"], metrics["ram_usage_percent"]]
    try:
        ai.train(values)
        return "KI erfolgreich trainiert mit: " + str(values)
    except Exception as e:
        return f"Fehler beim Training: {e}"

def test_ai_on_new_sample():
    metric = get_performance_metrics()["cpu_usage_percent"]
    try:
        return f"CPU: {metric}% → {ai.predict(metric)}"
    except Exception as e:
        return f"Fehler bei KI-Prüfung: {e}"

def gui_start_forensic_ki():
    try:
        start_forensic_ki()
        return "Forensik-KI gestartet."
    except Exception as e:
        return f"Fehler bei Forensik-KI: {e}"

def gui_start_tunnel():
    try:
        start_tunnel_for_forensics()
        return "Beta-Tunnel für Forensik gestartet."
    except Exception as e:
        return f"Tunnelstart fehlgeschlagen: {e}"

def run_setup_diagnostics():
    try:
        output = subprocess.check_output(["python3", "setup_check.py"], stderr=subprocess.STDOUT)
        return output.decode()
    except Exception as e:
        return f"Fehler beim Setup-Check: {e}"

def start_gui():
    root = tk.Tk()
    root.title("Pertinax Security Tool")
    apply_styles(root)
    load_icon(root)

    tk.Label(root, text="Willkommen im Pertinax Security Tool").pack(pady=10)

    tk.Button(root, text="📊 Systeminfo anzeigen", command=lambda: print(get_system_info())).pack(pady=3)
    tk.Button(root, text="📈 Performance prüfen", command=lambda: print(get_performance_metrics())).pack(pady=3)
    tk.Button(root, text="📍 Tracking starten", command=lambda: print(generate_mock_path())).pack(pady=3)
    tk.Button(root, text="🔐 SHA-256 erzeugen", command=lambda: print(sha256('test'))).pack(pady=3)
    tk.Button(root, text="🛡️ USB-Schutz prüfen", command=lambda: print(monitor_usb())).pack(pady=3)
    tk.Button(root, text="⚙️ Treiber prüfen", command=lambda: print(check_drivers())).pack(pady=3)
    tk.Button(root, text="🧠 KI trainieren (Systemdaten)", command=lambda: print(train_ai_with_system_data())).pack(pady=3)
    tk.Button(root, text="🤖 KI testen (CPU-Wert)", command=lambda: print(test_ai_on_new_sample())).pack(pady=3)
    tk.Button(root, text="🧬 Forensik-KI starten", command=lambda: print(gui_start_forensic_ki())).pack(pady=3)
    tk.Button(root, text="🛰️ Tunnel starten (Forensik)", command=lambda: print(gui_start_tunnel())).pack(pady=3)
    tk.Button(root, text="🧪 Diagnose starten (Setup)", command=lambda: print(run_setup_diagnostics())).pack(pady=3)

    root.mainloop()