
import json
import os

class LicenseManager:
    def __init__(self, license_file='config/license.json'):
        self.license_file = license_file
        self.license_data = {}

    def load_license(self):
        if os.path.exists(self.license_file):
            with open(self.license_file, 'r') as f:
                self.license_data = json.load(f)
                return self.license_data.get("valid", False)
        return False

    def register_license(self, key: str):
        self.license_data = {"key": key, "valid": True}
        with open(self.license_file, 'w') as f:
            json.dump(self.license_data, f)
        return True
