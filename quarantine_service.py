
import os
import shutil

class QuarantineService:
    def __init__(self, quarantine_dir='quarantine/'):
        self.quarantine_dir = quarantine_dir
        os.makedirs(self.quarantine_dir, exist_ok=True)

    def quarantine_file(self, filepath):
        if os.path.exists(filepath):
            filename = os.path.basename(filepath)
            shutil.move(filepath, os.path.join(self.quarantine_dir, filename))
            return True
        return False

    def list_quarantined_files(self):
        return os.listdir(self.quarantine_dir)
