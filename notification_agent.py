
import platform
import time

class NotificationAgent:
    def send_notification(self, message: str):
        print(f"[{time.strftime('%H:%M:%S')}] {platform.system()}-Notification: {message}")
