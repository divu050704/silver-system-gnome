import os
import subprocess
class color():
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   blued = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   silver = '\033[3;30;47m'
   orange= '\033[31;43m'
   bold = '\033[1m'
   green = '\033[32m'
   underline = '\033[4m'
   end = '\033[0m'
os.system('sudo nmap -sn 192.168.1.7/24')
ch = input(color.purple+'Do you want to ping any device(Y/n):\t'+color.end)
if ch == 'Y':
	ip = input(color.red+'Enter ip of device you want to ping:\t'+color.end)
	subprocess.run(['ping',ip])
	
