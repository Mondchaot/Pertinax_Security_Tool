
import tkinter as tk
from tkinter import messagebox

def launch_gui():
    root = tk.Tk()
    root.title("Pertinax Security Tool")
    root.geometry("600x400")
    tk.Label(root, text="Pertinax Security Tool GUI", font=("Courier", 16)).pack(pady=20)
    tk.Button(root, text="Antivirus Scan starten", command=lambda: messagebox.showinfo("Scan", "Antivirus-Scan gestartet")).pack(pady=10)
    root.mainloop()

if __name__ == '__main__':
    pass
