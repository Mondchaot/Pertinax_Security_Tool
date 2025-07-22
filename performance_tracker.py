
import time
import logging
import functools

class PerformanceTracker:
    @staticmethod
    def measure_performance(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            execution_time = time.time() - start_time
            if execution_time > 0.1:
                logging.warning(f"Performance-Warnung: {func.__name__} dauerte {execution_time:.4f}s")
            return result
        return wrapper
