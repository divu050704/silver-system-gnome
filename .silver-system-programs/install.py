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
	print(color.red+'1.\t'+color.green+'Install from apt'+color.end)# for installation from apt package manager
	print(color.red+'2.\t'+color.green+'Install from snap'+color.end)# for installation from snap package manager
	print(color.red+'3.\t'+color.green+'Install from git'+color.end)# Install any git repositery
	print(color.red+'4.\t'+color.green+'Instll from software center'+color.end)# GUI installation
	ch = int(input(color.purple+'Enter choice:\t'+color.end))
	if ch == 0:
		print(color.cyan+'Exiting.........'+color.end)
		exit()
	if ch == 1:
		software = input(color.yellow+'Enter the name of software:\t'+color.end)#Here it will take input from user for the package to install 
		search = subprocess.run(['sudo', 'apt', 'search',software])# First it will search any similar package or whether the package exists or not
		ch1= input(color.blue+'Do you want to continue installation(Y/n):\t'+color.end)#One last confirmation for installation
		if ch1 == 'Y':
				software1 = input(color.cyan+'Enter the final name of software for installations:\t'+color.end)#final confirmation name of the package
				install = subprocess.run(['sudo', 'apt', 'install',software1])#This command will install the package 
	if ch == 2:
		software = input(color.yellow+'Enter name of software:\t'+color.end)#Input packagee name from the user 
		search = subprocess.run(['sudo', 'snap', 'search',software])# It will first search any similar software or whether the package exists or not
		ch2 = input(color.blue+'Do you want to continue installation(Y/n):\t'+color.end)#final confirmation
		if ch2 == 'Y':
			software1 = input(color.cyan+'Enter the final name of softwre for installation:\t'+color.end)#One more time confirmation for package name 
			install = subprocess.run(['sudo', 'snap', 'install',software1])#main installation command
	if ch == 3:
		path = input(color.yellow+'Enter the path to installation:\t'+color.end)#In which directory you want to download git package
		software = input(color.blue+'Enter the link of the git software:\t')#link of the .git repostitory 
		os.chdir(path)#This will change the working directory
		install = subprocess.run(['git', 'clone',software])#main command for download repository  
	if ch == 4:
		os.system('gnome-software')#Just opens gnome-software centre

