import subprocess
ch = input('Do you want to continue:\t')
if ch == 'Y':
	path = input('Enter path of folder:\t')
	subprocess.run(['ls',path])
	
