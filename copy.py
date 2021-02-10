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
   orange= '\033[33m'
   bold = '\033[1m'
   green = '\033[32m'
   underline = '\033[4m'
   end = '\033[0m'
c = 'Y'
while c == "Y":
	path = input(color.red+'Enter path from root to the parent directory of the file:\t'+color.end)
	subprocess.run(['ls', path])
	file1 = input(color.purple+'Enter file name from root:\t'+color.end)
	dest = input(color.red+'Enter destination of file:\t'+color.end)
	subprocess.run(['ls', dest])
	file2 = input(color.purple+'Enter destination folder name from root:\t'+color.end)
	subprocess.run(['sudo','cp',file1,file2])
	c = input(color.blue+'Do you want to continue moving files(Y/n):\t'+color.end)


