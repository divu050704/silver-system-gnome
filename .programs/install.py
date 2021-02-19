import subprocess
import os
class color():
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   blued = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   silver = '\033[3;30;47m'
   orange= '\033[31;43m'
   bold = '\033[1m'
   green = '\033[32m'
   underline = '\033[4m'
   end = '\033[0m'
c = 'Y'
while c == 'Y':
	print(color.red+'0.\t'+color.green+'Exit'+color.end)
	print(color.red+'1.\t'+color.green+'Install from apt'+color.end)
	print(color.red+'2.\t'+color.green+'Install from snap'+color.end)
	print(color.red+'3.\t'+color.green+'Install from git'+color.end)
	print(color.red+'4.\t'+color.green+'Instll from software center'+color.end)
	ch = int(input(color.purple+'Enter choice:\t'+color.end))
	if ch == 0:
		print(color.cyan+'Exiting.........'+color.end)
		exit()
	if ch == 1:
		software = input(color.yellow+'Enter the name of software:\t'+color.end)
		search = subprocess.run(['sudo', 'apt', 'search',software])
		ch1= input(color.blue+'Do you want to continue installation(Y/n):\t'+color.end)
		if ch1 == 'Y':
				software1 = input(color.cyan+'Enter the final name of software for installations:\t'+color.end)
				install = subprocess.run(['sudo', 'apt', 'install',software1])
	if ch == 2:
		software = input(color.yellow+'Enter name of software:\t'+color.end)
		search = subprocess.run(['sudo', 'snap', 'search',software])
		ch2 = input(color.blue+'Do you want to continue installation(Y/n):\t'+color.end)
		if ch2 == 'Y':
			software1 = input(color.cyan+'Enter the final name of softwre for installation:\t'+color.end)
			install = subprocess.run(['sudo', 'snap', 'install',software1])
	if ch == 3:
		path = input(color.yellow+'Enter the path to installation:\t'+color.end)
		
		software = input(color.blue+'Enter the link of the git software:\t')
		os.chdir(path)
		install = subprocess.run(['git', 'clone',software])   
	if ch == 4:
		os.system('gnome-software')

