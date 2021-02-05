import os 
import subprocess
c = 'Y'
while c == "Y":
	path = input('Enter path from root to the parent directory of the file:\t')
	subprocess.run(['ls', path])
	file1 = input('Enter file name from root:\t')
	dest = input('Enter, destination of file:\t')
	subprocess.run(['ls', dest])
	file2 = input('Enter destination folder name from root:\t')
	subprocess.run(['sudo','cp',file1,file2])
	c = input('Do you want to continue moving files(Y/n):\t')

