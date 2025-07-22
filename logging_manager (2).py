import datetime

def write_log(entry, logfile="security.log"):
    with open(logfile, "a") as f:
        timestamp = datetime.datetime.now().isoformat()
        f.write(f"[{timestamp}] {entry}\n")