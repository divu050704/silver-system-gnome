import subprocess
import os
ch = 'Y'
while ch == 'Y':
	path = input('Enter path to the file till parent directory :\t')
	os.chdir(path)
	os.system('ls')
	file1 = input('Enter file name:\t')
	name = input('Enter keyword you want to search:\t')
	subprocess.run(['grep',name,file1])
	ch = input('Do you want to continue to search keywords(Y/n):\t')
