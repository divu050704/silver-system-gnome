import subprocess
ch = 'Y'
while ch == 'Y':
	file2 = input('Enter file name you want to serch:\t') 
	subprocess.run(['locate',file2])
	ch = input('Do you want to continue searching for files(Y/n):\t')
