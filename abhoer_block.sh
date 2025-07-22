
#!/bin/bash
echo 0 > /sys/class/video4linux/video0/device/enable 2>/dev/null
pactl unload-module module-loopback 2>/dev/null
