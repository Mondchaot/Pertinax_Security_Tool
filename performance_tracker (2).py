import psutil
import time

def get_performance_metrics():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "ram_usage_percent": psutil.virtual_memory().percent,
        "uptime_seconds": time.time() - psutil.boot_time()
    }