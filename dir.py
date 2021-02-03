import os 
ch = input('Do you want to continue(Y/n):\t')
if ch == 'Y':
	path = input('Enter where you want to go:\t')
	os.chdir(path)
	os.system('gnome-terminal')
