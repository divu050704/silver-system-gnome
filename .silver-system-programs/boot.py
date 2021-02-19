import os
class color():
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   blued = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   silver = '\033[3;30;47m'
   orange= '\033[33m'
   bold = '\033[1m'
   green = '\033[32m'
   underline = '\033[4m'
   end = '\033[0m'
cmd = os.system('systemd-analyze')
ch = input(color.purple+'Do you want blame chain(Y/n):\t'+color.end)
if ch == 'Y':
	cmd2 = os.system('systemd-analyze blame')
if ch == 'n':
	ch2 = input(color.purple+'Do you want critical-chain(Y/n):\t'+color.end)
	if ch2 == 'Y':
		cmd3 = os.system('systemd-analyze critical-chain')
