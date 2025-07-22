
#!/bin/bash
while true; do
    WIFI=$(nmcli radio wifi)
    BT=$(rfkill list bluetooth | grep -i 'Soft blocked: no')

    if [ "$WIFI" = "enabled" ]; then
        echo "[!] WLAN aktiv, deaktiviere..."
        nmcli radio wifi off
    fi

    if [ -n "$BT" ]; then
        echo "[!] Bluetooth aktiv, deaktiviere..."
        rfkill block bluetooth
    fi
    sleep 10
done
