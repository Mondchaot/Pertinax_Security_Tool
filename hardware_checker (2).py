
import platform
import psutil

class HardwareChecker:
    def check_components(self) -> dict:
        return {
            "cpu": platform.processor(),
            "ram": psutil.virtual_memory().total,
            "disk": psutil.disk_usage('/').total,
            "os": platform.system() + " " + platform.release()
        }

if __name__ == '__main__':
    pass
