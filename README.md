# Fast-Port-Scanner

This project is an Advanced Port Scanner with a Graphical User Interface (GUI) built using Python. The tool is designed to help network administrators and cybersecurity professionals identify open ports on a given target system. It leverages multi-threading for efficient and faster scanning, enabling the analysis of multiple ports concurrently.

# Key Features

## Graphical Interface:
The user-friendly GUI is built with the tkinter library.
Includes input fields for target IP address, starting port, and ending port range.

## Multi-Threaded Scanning:
The scanner uses multiple threads to handle large port ranges efficiently, reducing scan time significantly.

## Customizable Port Range:
Allows users to specify a range of ports (1-65535) to scan.

## Real-Time Output:
Displays scan progress and results in a scrollable text box for better readability.

## Error Handling:
Ensures valid input with checks for proper IP address formatting and valid port ranges.

## Author Acknowledgment:
Includes a footer label that credits the author: "Made by Yuvraj Singh Rangi".

# -------------------How It Works-------------------

1. The user enters the target IP address and specifies the range of ports to scan.
2. The application validates the inputs.
3. The scanning process begins, using threads to scan ports in parallel.
4. The tool identifies and lists all open ports, displaying them in the result box.
5. Upon completion, it shows the scan start and end times for reference.

# Use Cases

## Network Security:
Identify potential vulnerabilities by detecting open ports that can be exploited.

## Penetration Testing:
Analyze the security posture of a system by mapping open ports.

## Educational Tool:
Learn about port scanning and threading concepts in Python.

# Technologies Used

## Python Libraries:
1. socket: For network communication.
2. threading: To enable concurrent port scanning.
3. tkinter: To build the GUI.
4. queue: To manage ports efficiently during multi-threaded operations.
5. datetime: For timestamping scan start and end times.
