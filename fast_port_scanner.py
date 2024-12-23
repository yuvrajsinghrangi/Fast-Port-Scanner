import socket
import threading
import queue
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Set the number of threads for faster scanning
NUM_THREADS = 100

# Function to scan a single port
def scan_port(ip, port, result_queue):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout in seconds
        result = sock.connect_ex((ip, port))
        if result == 0:
            result_queue.put(port)
        sock.close()
    except socket.error:
        pass

# Worker function to handle threading
def worker(ip, port_queue, result_queue):
    while not port_queue.empty():
        port = port_queue.get()
        scan_port(ip, port, result_queue)
        port_queue.task_done()

# Function to perform the port scan with multi-threading
def scan_ports(ip, start_port, end_port, result_text):
    result_text.insert(tk.END, f"Scanning target: {ip}\n")
    result_text.insert(tk.END, f"Ports to scan: {start_port} - {end_port}\n")
    result_text.insert(tk.END, f"Scan started at: {datetime.now()}\n")
    result_text.yview(tk.END)  # Scroll to the bottom

    port_queue = queue.Queue()
    result_queue = queue.Queue()

    # Add ports to the queue
    for port in range(start_port, end_port + 1):
        port_queue.put(port)

    # Create threads to scan ports concurrently
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=worker, args=(ip, port_queue, result_queue))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Retrieve results
    open_ports = []
    while not result_queue.empty():
        open_ports.append(result_queue.get())

    if open_ports:
        result_text.insert(tk.END, f"\nOpen ports found: {open_ports}\n")
    else:
        result_text.insert(tk.END, "\nNo open ports found.\n")

    result_text.insert(tk.END, f"Scan completed at: {datetime.now()}\n\n")
    result_text.yview(tk.END)  # Scroll to the bottom

# Function to handle the scan button click
def on_scan_button_click():
    target_ip = ip_entry.get()
    try:
        socket.inet_aton(target_ip)
    except socket.error:
        result_text.insert(tk.END, "Invalid IP address format.\n")
        return

    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            result_text.insert(tk.END, "Invalid port range.\n")
            return
    except ValueError:
        result_text.insert(tk.END, "Please enter valid integers for port range.\n")
        return

    # Clear previous results
    result_text.delete(1.0, tk.END)

    # Call scan_ports to start the scanning process
    scan_ports(target_ip, start_port, end_port, result_text)

# Set up the main window
root = tk.Tk()
root.title("Port Scanner")
root.geometry("600x500")  # Increase window size for extra text at the bottom

# Label and Entry for IP address
ip_label = tk.Label(root, text="Enter Target IP Address:")
ip_label.pack(pady=5)
ip_entry = tk.Entry(root, width=40)
ip_entry.pack(pady=5)

# Label and Entry for Starting Port
start_port_label = tk.Label(root, text="Enter Starting Port:")
start_port_label.pack(pady=5)
start_port_entry = tk.Entry(root, width=40)
start_port_entry.pack(pady=5)

# Label and Entry for Ending Port
end_port_label = tk.Label(root, text="Enter Ending Port:")
end_port_label.pack(pady=5)
end_port_entry = tk.Entry(root, width=40)
end_port_entry.pack(pady=5)

# Scan Button
scan_button = tk.Button(root, text="Start Scan", command=on_scan_button_click)
scan_button.pack(pady=10)

# ScrolledText widget for displaying results
result_text = scrolledtext.ScrolledText(root, width=70, height=15, wrap=tk.WORD)
result_text.pack(pady=10)

# Label for "Made by Yuvraj Singh Rangi" at the bottom
made_by_label = tk.Label(root, text="Made by Yuvraj Singh Rangi", font=("Arial", 10, "italic"))
made_by_label.pack(side=tk.BOTTOM, pady=5)

# Start the GUI
root.mainloop()
