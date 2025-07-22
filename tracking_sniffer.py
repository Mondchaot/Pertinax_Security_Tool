import time
import random

# Realistischeres Mock-Tracking: simuliert Bewegung
def generate_mock_path(start_lat=48.137, start_lon=11.575, steps=5):
    path = []
    for i in range(steps):
        lat = start_lat + random.uniform(-0.0005, 0.0005)
        lon = start_lon + random.uniform(-0.0005, 0.0005)
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        path.append(f"{timestamp} | {lat:.6f}, {lon:.6f}")
        time.sleep(1)
    return path