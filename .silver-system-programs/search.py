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
ch = 'Y'
while ch == 'Y':
	path = input(color.purple+'Enter path to the file till parent directory :\t'+color.end)
	os.chdir(path)
	os.system('ls')
	file1 = input(color.cyan+'Enter file name:\t'+color.end)
	name = input(color.green+'Enter keyword you want to search:\t'+color.end)
	subprocess.run(['grep',name,file1])
	ch = input(color.red+'Do you want to continue to search keywords(Y/n):\t'+color.end)
