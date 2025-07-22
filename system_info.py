import platform
import psutil

def get_system_info():
    return {
        "system": platform.system(),
        "release": platform.release(),
        "cpu": platform.processor(),
        "ram": f"{psutil.virtual_memory().total / (1024**3):.2f} GB"
    }