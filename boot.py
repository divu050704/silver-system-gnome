import os
cmd = os.system('systemd-analyze')
ch = input('Do you want blame chain(Y/n):\t')
if ch == 'Y':
	cmd2 = os.system('systemd-analyze blame')
if ch == 'n':
	ch2 = input('Do you want critical-chain(Y/n):\t')
	if ch2 == 'Y':
		cmd3 = os.system('systemd-analyze critical-chain')
