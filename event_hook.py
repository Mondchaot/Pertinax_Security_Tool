
import win32file
import win32con

def monitor_directory(path):
    handle = win32file.CreateFile(
        path,
        win32con.FILE_LIST_DIRECTORY,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None,
        win32con.OPEN_EXISTING,
        win32con.FILE_FLAG_BACKUP_SEMANTICS,
        None
    )
    print("Monitoring gestartet für:", path)
