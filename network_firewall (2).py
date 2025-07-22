class NetworkFirewall:
    def is_blocked(self, ip_address):
        # Beispielimplementierung mit fester Blockliste
        blocked_ips = ["192.168.0.1", "10.0.0.1"]
        return ip_address in blocked_ips

    def add_rule(self, ip_address):
        if not hasattr(self, '_rules'):
            self._rules = []
        self._rules.append(ip_address)

if __name__ == '__main__':
    pass
