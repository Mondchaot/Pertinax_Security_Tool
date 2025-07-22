
from core.exceptions import DisplayAdapterException

class ConfigValidator:
    @staticmethod
    def validate_display_config(config):
        required_keys = ['resolution', 'color_scheme', 'scaling_factor']
        missing_keys = [key for key in required_keys if key not in config]
        if missing_keys:
            raise DisplayAdapterException(f"Fehlende Schlüssel: {missing_keys}", "CONFIG_001")
        if not (0.5 <= config.get('scaling_factor', 1) <= 2.0):
            raise DisplayAdapterException(f"Ungültiger Skalierungsfaktor", "CONFIG_002")
        return config
