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
ch = 'Y'
while ch == 'Y':
	print(color.yellow+'In which format you want information'+color.end)
	print(color.red+'0.\t'+color.green+'Exit'+color.end)
	print(color.red+'1.\t'+color.green+'Megabyte'+color.end)
	print(color.red+'2.\t'+color.green+'Bytes'+color.end)
	y = int(input(color.purple+'Enter your choice:\t'+color.end))
	if y == 0:
		print(color.cyan+'Exiting................'+color.end)
	if y == 1:
		os.system('df -m')
	if y == 2:
		os.system('df')
	ch = input(color.orange+color.bold+'Do you want to continue seeing disk informations in different formats(Y/n):\t'+color.end)
