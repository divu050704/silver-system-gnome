import os
import subprocess
terminal = os.system('sudo nmap -sn 192.168.1.7/24')
ch = input('Do you want to ping any device(Y/n):\t')
if ch == 'Y':	
	ip = input('Enter ip of device you want to ping:\t')
	subprocess.run(['ping',ip])
	if KeyboardInterrupt:
		exit()	
	
