
import logging
from datetime import datetime
import traceback

class DisplayAdapterException(Exception):
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        self.timestamp = datetime.now()
        self.trace = traceback.format_exc()
        self.log_error()

    def log_error(self):
        logging.error(f"[{self.timestamp}] Code {self.error_code}: {self.message}")
