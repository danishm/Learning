import tkinter as tk
from tkinter import ttk
import time
import psutil

# Function to update system information
def update_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    
    cpu_label.config(text=f"CPU: {cpu_usage:.1f}%")
    ram_label.config(text=f"RAM: {ram_usage:.1f}%")
    disk_label.config(text=f"Disk: {disk_usage:.1f}%")
    
    # Schedule next update
    window.after(1000, update_info)

# Initialize the main window
window = tk.Tk()
window.title("System Info")
window.geometry("200x100")

# Create labels for system information
cpu_label = tk.Label(window, text="CPU: 0%")
cpu_label.pack()
ram_label = tk.Label(window, text="RAM: 0%")
ram_label.pack()
disk_label = tk.Label(window, text="Disk: 0%")
disk_label.pack()

# Start updating information
update_info()

# Run the main loop
window.mainloop()