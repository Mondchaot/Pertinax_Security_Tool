import time
import logging

class PerformanceTracker:
    @staticmethod
    def measure(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            duration = time.time() - start
            logging.info(f"Execution time: {duration:.4f}s")
            return result
        return wrapper