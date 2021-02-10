import os 
import subprocess
class color:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   blued = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   silver = '\033[1;30;40m'
   orange = '\033[33m'
   green = '\033[32m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'
c = 'Y'
while c == "Y":
	path = input(color.purple+'Enter path from root to the file:\t'+color.end)
	subprocess.run(['ls',path])
	file1 = input(color.green+'Enter file name with full directories:\t'+color.end)
	dest = input(color.purple+'Enter destination of file:\t'+color.end)
	subprocess.run(['ls',dest])
	file2 = input(color.green+'Enter file name with full directories:\t'+color.end)
	subprocess.run(['sudo','mv',file1,file2])
	c = input(color.bold+color.blued+'Do you want to continue moving files(Y/n):\t'+color.end)
