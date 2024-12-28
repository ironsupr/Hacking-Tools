# Brute Force Login Script

This Python script is designed to brute-force the login credentials of a website. It works by iterating through a list of possible passwords and attempting to log in using a specific username. If the login fails, the script moves to the next password. If the login is successful, it will display the username and password found.

## Requirements

- Python 3.x
- `requests` library for making HTTP requests
- `termcolor` library for colored terminal output

You can install the required libraries by running:

```bash
pip install requests termcolor
```

## Script Usage

### Steps to Run the Script

1. **Run the Script**:

   After making sure you have installed the required libraries, run the script:

   ```bash
   python Bruteforce.py
   ```

2. **Provide Inputs**:

   The script will prompt you for the following inputs:

   - **Page URL**: Enter the URL of the login page.
   - **Username**: Enter the username you want to attempt to brute-force (e.g., admin, user123).
   - **Password File**: Provide the path to the text file that contains the list of possible passwords (one per line).
   - **Login Failure String**: Enter the string that is present in the HTML response when the login attempt fails (e.g., "Invalid username or password").
   - **Cookie Value (Optional)**: If the website requires a session cookie, you can provide it here. This is optional, and you can leave it empty if not required.

### Example

```bash
[+] Enter Page URL: https://example.com/login
[+] Enter Username For The Account To BruteForce: admin
[+] Enter Password File To Use: passwords.txt
[+] Input The String That Occurs When Login Fails: Invalid login
[+] Enter Cookie Value (Optional): (Leave Empty If Not Needed)
```

### Password Brute-Force

After entering the inputs, the script will start trying each password from the list. If it finds a correct password, it will print the username and password:

```bash
[+] Found Username: ==> admin
[+] Found Password: ==> password123
```

### No Match

If none of the passwords work, it will print:

```bash
[!!] Password Not In List
```

### Important: Customization for Different Websites

To make this script work for different websites, you might need to modify certain parts of the code to match the structure of the target site's login page. Here’s what you should look at:

1. **Form Data**:

   The script currently assumes that the form for login uses the following field names:
   - `username`
   - `password`
   - `Login`

   If the target website has different form field names, you will need to adjust the data dictionary in the `cracking()` function.

   ```python
   data = {'username_field': username, 'password_field': password, 'login_button': 'Login'}
   ```

2. **HTTP Request Type (GET or POST)**:

   The script currently supports both GET and POST requests, but it defaults to POST if no cookie value is provided.

   If the target site uses a GET request for login, you can modify the request to use GET and include the form parameters in the URL:

   ```python
   response = requests.get(url, params={'username': username, 'password': password, 'Login': 'Login'}, cookies={'Cookie': cookie_value})
   ```

3. **Login Failure Detection**:

   The `login_fail_string` variable is used to detect when a login attempt fails by checking if a certain string is present in the response body.

   You should inspect the login failure response on the website to find a string that is included when the login fails (such as "Invalid credentials", "Incorrect password", etc.).

   You can adjust the `login_fail_string` to match this error message or part of it. For example, if the website returns "Incorrect password" on failure, you would set:

   ```bash
   [+] Input The String That Occurs When Login Fails: Incorrect password
   ```

4. **Session Cookies**:

   Some websites require session cookies for login to function properly, especially if the site uses sessions to track user state after login.

   If you have a session cookie, you can pass it into the `requests` library like this:

   ```python
   response = requests.get(url, params=data, cookies={'Cookie': cookie_value})
   ```

   If cookies are not needed, simply leave the cookie input empty.

### Example Adjustments

Here's an example of a typical login form and how to adjust the script:

**Login Form HTML Example**:

```html
<form action="login.php" method="POST">
  <input type="text" name="user" placeholder="Username">
  <input type="password" name="passwd" placeholder="Password">
  <button type="submit">Login</button>
</form>
```

**Adjustments to the Script**:

Change the field names to match the form:

```python
data = {'user': username, 'passwd': password, 'Login': 'Login'}
```

Make sure the failure string matches the message shown when login fails. If the message on the page is "Login failed", use that string:

```bash
login_fail_string = 'Login failed'
```

### Disclaimer

Use this script responsibly. Unauthorized use of this script for hacking or attacking websites is illegal and unethical. Make sure you have permission to perform security testing on the target website. This script is intended for educational purposes only and should only be used in controlled, ethical environments (e.g., testing your own applications, participating in bug bounty programs, or pentesting with authorization).

---
