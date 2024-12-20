import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading

def set_alarm():
    alarm_time = alarm_time_entry.get()
    if alarm_time:
        try:
            # Validate time format
            datetime.strptime(alarm_time, "%H:%M:%S")
            status_label.config(text=f"Alarm set for {alarm_time}")
            threading.Thread(target=alarm_thread, args=(alarm_time,), daemon=True).start()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format.")
    else:
        messagebox.showwarning("No Time Entered", "Please enter a time.")

def alarm_thread(alarm_time):
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time to wake up!")
            break
        time.sleep(1)

# Create the main window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x200")

# Widgets
instruction_label = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
instruction_label.pack(pady=10)

alarm_time_entry = tk.Entry(root, font=("Helvetica", 14), justify="center")
alarm_time_entry.pack(pady=5)

set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm)
set_alarm_button.pack(pady=10)

status_label = tk.Label(root, text="", font=("Helvetica", 10), fg="green")
status_label.pack(pady=10)

# Run the application
root.mainloop()
