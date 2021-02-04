import os
import subprocess
print('Is it a file or a folder???')
print('0.\t Exit')
print('1.\t File')
print('2.\t Folder')
y= 'Y'
while y == 'Y':
	ch = int(input('Enter your choice:\t'))
	if ch == 0:
		exit()
	if ch == 1:
		c = 'Y'
		while c == 'Y':
			path = input('Enter path to file:\t')
			print('Files in ',path,':-')
			os.chdir(path)
			subprocess.run(['ls'])
			c1 = input('Do you want to continue removing file(Y/n):\t')
			if c1 == 'Y':
				os.chdir(path)
				file1 = input('Enter file name:\t')
				subprocess.run(['sudo','rm','file1'])
			c = input('Do you want to continue removing files(Y/n):\t')
	if ch == 2:
		c2 = 'Y'
		while c2 == 'Y':
			path1 = input('Enter path to folder:\t')
			print('Folders an files in',path1,':-')
			os.chdir(path1)
			os.system('ls')
			c3 = input('Do you want to continue(Y/n):\t') 
			if c3 == 'Y':
				os.chdir(path1)
				folder = input('Enter folder name:\t')
				subprocess.run(['sudo','rm','-r',folder])
			c2 = input('Do you want to continue removing folder(Y/n):\t')					
	y = input('Do you want to continue removing files and folders(Y/n):\t')
