import subprocess
import platform
import tkinter as tk
from tkinter import filedialog

def list_background_processes():
    processes = []
    try:
        operating_system = platform.system()

        if operating_system == 'Windows':
            output = subprocess.check_output(["tasklist"], text=True)
            lines = output.strip().split('\n')[3:]  # Skip the first 3 lines of the header
            for line in lines:
                fields = line.split()
                pid = fields[1]
                name = fields[0]
                processes.append((pid, name))

        elif operating_system == 'Linux':
            output = subprocess.check_output(["ps", "-e"], text=True)
            lines = output.strip().split('\n')[1:]  # Skip the header
            for line in lines:
                fields = line.split()
                pid = fields[0]
                name = fields[-1]
                processes.append((pid, name))

        # Add support for other operating systems if needed
        else:
            print("Unsupported operating system.")

    except subprocess.CalledProcessError as e:
        processes.append(("Error", "Unable to get process list"))

    return processes

def update_processes_list():
    background_processes = list_background_processes()
    process_list.delete(0, tk.END)  # Clear the listbox
    for pid, name in background_processes:
        process_list.insert(tk.END, f"PID: {pid}, Name: {name}")

def save_to_file():
    background_processes = list_background_processes()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as file:
            for pid, name in background_processes:
                file.write(f"PID: {pid}, Name: {name}\n")

# Tkinter GUI
root = tk.Tk()
root.title("Background Processes")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

process_list = tk.Listbox(frame, width=40, height=15)
process_list.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=process_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
process_list.config(yscrollcommand=scrollbar.set)

refresh_button = tk.Button(root, text="Refresh Processes", command=update_processes_list)
refresh_button.pack()

save_button = tk.Button(root, text="Save to File", command=save_to_file)
save_button.pack()

update_processes_list()  # Initial population of the process list

root.mainloop()