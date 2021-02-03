import os
cmd = os.system('sudo apt update && sudo apt  list --upgradable -a')
ch = input('Do you want to upgrade(Y/n):\t')
if ch == 'Y':
	cmd2 = os.system('sudo apt upgrade')
else:
	exit()
