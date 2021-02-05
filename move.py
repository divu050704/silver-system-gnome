import os 
import subprocess
c = 'Y'
while c == "Y":
	path = input('Enter path from root to the file:\t')
	dest = input('Enter destination of file:\t')
	y = input('Do you want to continue(Y/n):\t')
	if y == 'Y':
		subprocess.run(['sudo','mv',path,dest])
	c = input('Do you want to continue moving files(Y/n):\t')
