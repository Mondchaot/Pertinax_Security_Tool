
import requests
from bs4 import BeautifulSoup
import hashlib
import logging
from datetime import datetime
import pdfkit
import os

class PhishingTracker:
    def __init__(self):
        self.suspicious_sites_db = set()
        self.malware_signatures = self.load_signatures()
        self.logger = logging.getLogger('phishing_tracker')

    def load_signatures(self):
        return {
            'phishing_patterns': [r'steal.*credential', r'cookie.*theft', r'track.*user'],
            'malware_indicators': ['obfuscated_script', 'hidden_iframe', 'suspicious_redirect']
        }

    def analyze_webpage(self, url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            scripts = soup.find_all('script')
            tracking_scripts = self.detect_tracking_scripts(scripts)
            cookies = self.extract_cookies(response.headers)
            suspicious_cookies = self.analyze_cookies(cookies)
            return {
                'tracking_scripts': tracking_scripts,
                'suspicious_cookies': suspicious_cookies,
                'malware_risk': self.calculate_malware_risk(soup)
            }
        except requests.RequestException as e:
            self.logger.error(f"Fehler bei URL-Analyse: {e}")
            return None

    def detect_tracking_scripts(self, scripts):
        suspicious_scripts = []
        for script in scripts:
            script_content = script.string or script.get('src', '')
            if any(re.search(pattern, script_content, re.IGNORECASE) for pattern in self.malware_signatures['phishing_patterns']):
                suspicious_scripts.append({'content': script_content, 'hash': hashlib.md5(script_content.encode()).hexdigest()})
        return suspicious_scripts

    def extract_cookies(self, headers):
        cookies = {}
        cookie_header = headers.get('Set-Cookie', '')
        for cookie in cookie_header.split(';'):
            if '=' in cookie:
                name, value = cookie.strip().split('=', 1)
                cookies[name] = value
        return cookies

    def analyze_cookies(self, cookies):
        suspicious_cookies = []
        for name, value in cookies.items():
            if self.is_suspicious_cookie(name, value):
                suspicious_cookies.append({'name': name, 'value': value, 'risk_score': self.calculate_cookie_risk(value)})
        return suspicious_cookies

    def is_suspicious_cookie(self, name, value):
        # Dummy check for suspicious cookie names or values
        suspicious_keywords = ['track', 'session', 'id']
        return any(keyword in name.lower() for keyword in suspicious_keywords)

    def calculate_cookie_risk(self, value):
        # Dummy risk score based on length
        return min(len(value) / 100, 1.0)

    def calculate_malware_risk(self, soup):
        risk_factors = [
            len(soup.find_all('iframe', src=True)),
            len(soup.find_all('script', src=lambda x: x and 'unknown' in x)),
            soup.text.count('eval('),
            soup.text.count('document.write')
        ]
        return sum(risk_factors) / 10

def main():
    import sys
    print("Pertinax Security Tool - Windows Version")
    if len(sys.argv) < 2:
        print("Bitte URL als Argument eingeben.")
        return
    url = sys.argv[1]
    tracker = PhishingTracker()
    result = tracker.analyze_webpage(url)
    if result:
        print(f"Analyse Ergebnis für {url}:")
        print(result)
    else:
        print("Analyse fehlgeschlagen.")

if __name__ == "__main__":
    main()
