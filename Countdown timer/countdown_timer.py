import tkinter as tk
from tkinter import messagebox
import time

# Function to start the countdown
def start_countdown():
    try:
        # Get the time in seconds
        total_seconds = int(entry_time.get())

        # If the input is not valid (negative number), show an error
        if total_seconds < 0:
            messagebox.showerror("Error", "Please enter a positive integer")
            return

        # Countdown logic
        while total_seconds > 0:
            # Calculate minutes and seconds
            mins, secs = divmod(total_seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label_time.config(text=time_format)
            root.update()
            time.sleep(1)
            total_seconds -= 1

        label_time.config(text="Time's up!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

# Creating main window
root = tk.Tk()
root.title("Countdown Timer")

# Input for time in seconds
label_prompt = tk.Label(root, text="Enter time in seconds:")
label_prompt.pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)

# Display for countdown time
label_time = tk.Label(root, text="00:00", font=("Helvetica", 48))
label_time.pack(pady=20)

# Start button
button_start = tk.Button(root, text="Start", command=start_countdown)
button_start.pack(pady=5)

root.mainloop()
