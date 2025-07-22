class PhishingSniffer:
    def run_analysis(self, url):
        # Primitive Regel: Enthält URL das Wort "phishing", gilt es als verdächtig
        return "phishing" in url.lower()

    def initialize(self):
        self._initialized = True
