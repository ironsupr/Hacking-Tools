import socket
from termcolor import colored


def scan_port(ipaddress,port):
	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		print("[+] Port Opened " + str(port))
		sock.close()
	except:
#		print("[-] Port Closed " + str(port))
		pass

def scan(target, ports):
	print('\n'+'Starting Scan For ' + str(target))
	for port in range(1, int(ports)):
		scan_port(target, port)


targets = input("[*] Enter Targets To Scan(Split Them By Comma(,): ")
ports = input("[*] Enter How Many Ports You Want To Scan: ")

if ',' in targets:
	print('[*] Scanning Multiple Targets')
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets, ports)