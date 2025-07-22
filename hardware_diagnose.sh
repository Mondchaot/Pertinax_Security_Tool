
#!/bin/bash
echo "[i] Starte Hardware-Scan..."
echo "- CPU Info:"
lscpu | grep 'Model name'
echo "- RAM Speicher:"
free -h
echo "- GPU:"
lspci | grep VGA
echo "- Speicherlaufwerke:"
lsblk
echo "- WLAN Status:"
nmcli dev status | grep wifi
echo "- Bluetooth Status:"
rfkill list
echo "[i] Hardwareprüfung abgeschlossen."
