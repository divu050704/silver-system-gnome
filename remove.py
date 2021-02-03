import os
import subprocess
print('From which software you want to remove:-')
print('1.\t apt')
print('2.\t snap')
ch = int(input('Enter your choice:\t'))
c = 'Y'
while c == 'Y':
	if ch == 1 :
		software = input('Enter name of the software you want to remove:\t')
		y = input('Do you want to continue removing above software (Y/n):\t')
		while y == 'Y':
			subprocess.run(['sudo', 'apt','remove',software])
		
	if ch == 2 :
		software = input('Enter name of the software:\t')
		y1 = input('Do you want to continue removing above software (Y/n):\t')
		while y1 == 'Y':
			subprocess.run(['sudo','snap','remove',software])
	y2 = input('Do you want to perform autoremove(Y/n):\t')
	if y2 == 'Y':
		os.system('sudo apt autoremove')
	c= input('Do you want to continue removing other softwares(Y/n):\t')
