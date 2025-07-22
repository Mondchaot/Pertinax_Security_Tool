
from mitmproxy import http

def response(flow: http.HTTPFlow) -> None:
    if "set-cookie" in flow.response.headers:
        cookies = flow.response.headers.get_all("set-cookie")
        for cookie in cookies:
            if any(s in cookie.lower() for s in ["sessionid", "token", "auth"]):
                print(f"[!] Sensitiver Cookie entdeckt: {cookie}")
                if "phishing" in flow.request.pretty_url:
                    print("[!] Möglicher Phishingversuch!")
    filename = flow.request.path.lower()
    if any(filename.endswith(ext) for ext in [".exe", ".bat", ".zip", ".rar", ".js"]):
        print(f"[!] Möglicher Schadcode-Download: {filename}")
        flow.response = http.HTTPResponse.make(403, b"Download blockiert.", {})
