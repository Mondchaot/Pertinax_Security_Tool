
import os
import hashlib

class BehaviorAnalyzer:
    def analyze_file(self, filepath):
        if not os.path.exists(filepath):
            return "Datei existiert nicht"

        try:
            with open(filepath, "rb") as f:
                data = f.read()
            hash_val = hashlib.sha256(data).hexdigest()
            if "eval" in data.decode(errors="ignore"):
                return f"Warnung: Datei enthält potenziell gefährliche Inhalte (Hash: {hash_val})"
            return "Unauffällig"
        except Exception as e:
            return f"Fehler bei der Analyse: {e}"
