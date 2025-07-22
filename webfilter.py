
import re

class WebFilter:
    def __init__(self):
        self.blocked_domains = ["ads.example.com", "malware.site", "tracker.bad"]

    def is_blocked(self, url: str) -> bool:
        for domain in self.blocked_domains:
            if domain in url:
                return True
        return False

    def add_block(self, domain: str):
        if domain not in self.blocked_domains:
            self.blocked_domains.append(domain)

    def remove_block(self, domain: str):
        if domain in self.blocked_domains:
            self.blocked_domains.remove(domain)
