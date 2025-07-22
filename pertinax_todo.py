
import tkinter as tk
from tkinter import ttk

tasks = [
    ("BadUSB-Erkennung", False),
    ("Keylogger-Schutz", False),
    ("Phishing-Sniffer", False),
    ("Performance-Analyse", False),
    ("Forensik-Tool", False),
    ("KI-Modul-Verknüpfung", False),
    ("USB-Angriffsblocker", False),
    ("Polizei-Link-Entfernung", True),
]

class ToDoApp:
    def __init__(self, root):
        root.title("Pertinax Security – To-Do-Liste")
        root.configure(bg='#50C878')  # Smaragdgrün
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TCheckbutton", background="#50C878", font=("Courier New", 10))
        
        for i, (task, completed) in enumerate(tasks):
            var = tk.BooleanVar(value=completed)
            chk = ttk.Checkbutton(root, text=task, variable=var)
            chk.grid(row=i, column=0, sticky="w", padx=10, pady=2)

        export_btn = tk.Button(root, text="PDF-Export", bg="black", fg="white", font=("Courier New", 10))
        export_btn.grid(row=len(tasks)+1, column=0, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
