
import psutil
import json
from datetime import datetime

def log_memory_snapshot():
    memory = psutil.virtual_memory()
    snapshot = {
        "timestamp": datetime.now().isoformat(),
        "total_MB": memory.total // 1024 // 1024,
        "used_MB": memory.used // 1024 // 1024,
        "percent": memory.percent
    }
    with open("logs/memory_log.json", "a") as f:
        json.dump(snapshot, f)
        f.write("\n")
