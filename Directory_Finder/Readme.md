Here's a simple README file for the script you provided, explaining how to use it:

---

# Directory Brute-Forcer

This is a simple Python script to discover hidden directories in a target website by making requests to each directory listed in a file. It helps security researchers and ethical hackers identify potential unlisted directories on a website.

## Prerequisites

Before running this script, ensure that you have the following:

- Python 3.x installed.
- `requests` library installed. You can install it using pip if you don't have it:

```bash
pip install requests
```

## How to Use

1. **Prepare the directories list**: Create a text file that contains a list of directory names (one per line) that you want to check for on the target URL. For example, you might create a file called `directories.txt` with directory names like:

```
admin
login
uploads
images
private
```

2. **Run the Script**: Open a terminal or command prompt and navigate to the directory where the script is located. Then, run the script with:

```bash
python directory_bruteforce.py
```

3. **Provide Inputs**: 
    - The script will prompt you to enter the **Target URL** of the website you want to scan (e.g., `example.com`).
    - It will then ask for the **Name of the file** containing the list of directories you want to check (e.g., `directories.txt`).

4. **View Results**: If any directory is discovered on the target URL, the script will display the discovered directory path in the terminal, like so:

```bash
[*] Discovered Directory At This Path: http://example.com/admin
```

## How the Script Works

- **Target URL**: The script appends each directory name (from the provided file) to the target URL.
- **Request**: It sends a GET request to each resulting URL.
- **Response**: If the response is successful (i.e., the directory exists), the script prints the full URL of the discovered directory.

## Example Usage

```bash
[*] Enter Target URL: example.com
[*] Enter Name Of Files Containing Directories: directories.txt
[*] Discovered Directory At This Path: http://example.com/admin
[*] Discovered Directory At This Path: http://example.com/uploads
```

## Notes

- The script only checks for directories listed in the provided file. It does not attempt to guess any other directories.
- You may want to use this script on websites where you have explicit permission to do so.
- The script doesn't check for subdirectories or any other hidden paths beyond the ones listed in the provided file.

## License

This script is for educational purposes and should only be used with permission on websites where you are authorized to perform security testing.

---