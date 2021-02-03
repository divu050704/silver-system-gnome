import subprocess
import os
print('1.\t Install from apt')
print('2.\t Install from snap')
print('3.\t Install from git')
print('4.\t Instll from software center')
ch = int(input('Enter choice:\t'))
if ch == 1:
	software = input('Enter the name of software:\t')
	search = subprocess.run(['sudo', 'apt', 'search',software])
	ch1= input('Do you want to continue installation(Y/n):\t')
	if ch1 == 'Y':
			software1 = input('Enter the final name of software for installations:\t')
			install = subprocess.run(['sudo', 'apt', 'install',software1])
if ch == 2:
	software = input('Enter name of software:\t')
	search = subprocess.run(['sudo', 'snap', 'search',software])
	ch2 = input('Do you want to continue installation(Y/n):\t')
	if ch2 == 'Y':
		software1 = input('Enter the final name of softwre for installation:\t')
		install = subprocess.run(['sudo', 'snap', 'install',software1])
if ch == 3:
	path = input('Enter the path to installation:\t')
	os.chdir = path
	software = input('Enter the link of the git software:\t')
	install = subprocess.run(['git', 'clone',software])   
if ch == 4:
	os.system('gnome-software')

