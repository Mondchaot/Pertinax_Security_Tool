
# Datei: deep_packet_monitor.py
import socket

def start_packet_monitor():
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
    sock.bind(("0.0.0.0", 0))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

    print("Starte Deep Packet Monitoring...")
    while True:
        data, addr = sock.recvfrom(65565)
        print(f"Paket von {addr}: {data[:60]}...")

if __name__ == "__main__":
    start_packet_monitor()
