import socket

class CustomTCPProtocol:
    def __init__(self, host='0.0.0.0', port=9000):
        self.host = host
        self.port = port

    def start_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server läuft auf {self.host}:{self.port}")
            conn, addr = s.accept()
            with conn:
                print(f"Verbindung von {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print("Empfangen:", data)
                    conn.sendall(b'Daten empfangen')

if __name__ == '__main__':
    server = CustomTCPProtocol()
    server.start_server()
