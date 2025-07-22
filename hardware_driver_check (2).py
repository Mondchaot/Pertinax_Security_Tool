import platform

def check_drivers():
    system = platform.system()
    drivers = []

    if system == "Windows":
        drivers = ["usb.sys", "pci.sys", "acpi.sys"]
    elif system == "Linux":
        drivers = ["/dev/sda", "/dev/input/event0", "/dev/video0"]
    elif system == "Darwin":
        drivers = ["/System/Library/Extensions/AppleUSB.kext"]
    else:
        drivers = ["Unknown OS"]

    found = [d for d in drivers if True]  # Hier könnte man existenzprüfen
    return {"OS": system, "Treiber": found}