
#!/bin/bash
iptables -A OUTPUT -p tcp --dport 4444 -j DROP
iptables -A OUTPUT -d 203.0.113.42 -j DROP
iptables -A OUTPUT -j LOG --log-prefix "FIREWALL OUT: "
