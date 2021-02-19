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
	path = input(color.purple+'Enter path to parent directory:\t'+color.yellow)
	os.chdir(path)
	print(color.red+'Files in',path+color.green)
	os.system('ls')
	file1= input(color.darkcyan+'Enter file name you want to copy:\t'+color.yellow)
	target = input(color.purple+'Enter path to destination:\t'+color.yellow)
	subprocess.run(['cp',file1,target])
	print(color.red+'Files in ',target+color.green)
	subprocess.run(['ls',target])
	c = input(color.bold+color.blue+'Do you want to continue coping files(Y/n):\t'+color.end) 
	
