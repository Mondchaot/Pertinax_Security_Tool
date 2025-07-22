import logging
from datetime import datetime

class DisplayAdapterException(Exception):
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()

    def log_error(self):
        logging.error(f"[{self.timestamp}] Error ({self.error_code}): {self.message}")