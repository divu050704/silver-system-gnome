import os
import subprocess
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
	print(color.yellow+'From which software you want to remove:-'+color.end)
	print(color.red+'1.\t'+color.green+'apt'+color.end)
	print(color.red+'2.\t'+color.green+'snap'+color.end)
	ch = int(input(color.purple+'Enter your choice:\t'+color.end))
	if ch == 1 :
		software = input(color.cyan+'Enter name of the software you want to remove:\t'+color.end)
		y = input(color.purple+'Do you want to continue removing above software (Y/n):\t'+color.end)
		while y == 'Y':
			subprocess.run(['sudo', 'apt','remove',software])
		
	if ch == 2 :
		software = input(color.cyan+'Enter name of the software:\t'+color.end)
		y1 = input(color.purple+'Do you want to continue removing above software (Y/n):\t'+color.end)
		while y1 == 'Y':
			subprocess.run(['sudo','snap','remove',software])
	y2 = input(color.darkcyan+'Do you want to perform autoremove(Y/n):\t'+color.end)
	if y2 == 'Y':
		os.system('sudo apt autoremove')
	c= input(color.bold+color.blued+'Do you want to continue removing other softwares(Y/n):\t')
