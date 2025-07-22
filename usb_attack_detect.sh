
#!/bin/bash
dmesg | grep -i usb | grep -E 'reset|over-current|error' > usb_attack_log.txt
echo "[i] USB-Angriffe aufgezeichnet in usb_attack_log.txt"
