import socket

class BetaTunnel:
    def __init__(self, local_port=9999, target_host="127.0.0.1", target_port=8888):
        self.local_port = local_port
        self.target_host = target_host
        self.target_port = target_port

    def start_forwarding(self):
        print(f"[Tunnel] Leite Verkehr von localhost:{self.local_port} → {self.target_host}:{self.target_port}")
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(("0.0.0.0", self.local_port))
        server.listen(5)
        while True:
            client_socket, _ = server.accept()
            data = client_socket.recv(4096)
            if data:
                response = self._relay_to_target(data)
                client_socket.sendall(response)
            client_socket.close()

    def _relay_to_target(self, data):
        try:
            with socket.create_connection((self.target_host, self.target_port)) as s:
                s.sendall(data)
                return s.recv(4096)
        except Exception as e:
            return f"[Tunnel Error] {e}".encode()