import logging
from datetime import datetime

class PertinaxException(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        self.timestamp = datetime.now()
        logging.error(f"[{self.timestamp}] {code}: {message}")
