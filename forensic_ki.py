from ai_analyzer import AIAnalyzer
from performance_tracker import get_performance_metrics
from beta_tunnel_router import BetaTunnel
import threading

def start_forensic_ki():
    ai = AIAnalyzer()
    values = [get_performance_metrics()["cpu_usage_percent"], get_performance_metrics()["ram_usage_percent"]]
    ai.train(values)
    print("[Forensik-KI] Trainiert mit Systemdaten:", values)
    print("[Forensik-KI] Test: ", ai.predict(get_performance_metrics()["cpu_usage_percent"]))

def start_tunnel_for_forensics():
    tunnel = BetaTunnel(local_port=7070, target_host="127.0.0.1", target_port=8080)
    threading.Thread(target=tunnel.start_forwarding).start()