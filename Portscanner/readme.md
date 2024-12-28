# Port Scanner

This Python script allows you to scan multiple targets for open ports using a specified range of ports. It helps identify open ports on target IP addresses for security assessment and network troubleshooting.

## Requirements

- Python 3.x
- `termcolor` library for colored terminal output

You can install the required library by running:

```bash
pip install termcolor
```

## Usage

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ironsupr/Hacking-Tools/tree/main/Portscanner
   cd Portscanner
   ```

2. **Run the Script**:

   ```bash
   python Portscanner.py
   ```

3. **Provide Inputs**:

   The script will prompt you for the following inputs:

   - **Targets**: Enter the IP addresses to scan, separated by commas (e.g., `192.168.1.1, 192.168.1.2`).
   - **Number of Ports**: Enter the number of ports to scan (e.g., `100` to scan ports 1-100).

### Example

```bash
[*] Enter Targets To Scan (Split Them By Comma(,)): 192.168.1.1, 192.168.1.2
[*] Enter How Many Ports You Want To Scan: 100
```

### Script Output

The script will start scanning the specified targets and output the open ports:

```bash
Starting Scan For 192.168.1.1
[+] Port Opened 22
[+] Port Opened 80

Starting Scan For 192.168.1.2
[+] Port Opened 22
[+] Port Opened 443
```

## How It Works

- The `scan_port` function attempts to connect to the specified IP address and port.
- If the connection is successful, it prints that the port is open.
- The `scan` function iterates through the specified range of ports for each target IP address.

## Disclaimer

This script is intended for educational purposes only. Unauthorized use of this script for scanning networks or systems without permission is illegal and unethical. Use this tool responsibly and only on networks and systems you have explicit permission to test.

---