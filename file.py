import subprocess
ch = 'Y'
while ch == 'Y':
	path = input('Enter path of folder:\t')
	subprocess.run(['ls',path])
	ch = input('Do you want to continue(Y/n):\t')
