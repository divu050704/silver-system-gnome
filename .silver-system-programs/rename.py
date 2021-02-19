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
	parent = input(color.green+'Enter parent directory of file:\t'+color.end)
	os.chdir(parent)
	os.system('ls')
	file1 = input(color.purple+'Enter file name you want to rename:\t'+color.end)
	file2 = input(color.red+'Enter new file name:\t'+color.end)
	subprocess.run(['mv',file1,file2])
	print(color.darkcyan+'Name changed:-'+color.end)
	os.system('ls')
	ch = input(color.bold+color.cyan+'Do you want to continue renaming files(Y/n):\t'+color.end)
