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

y= 'Y'
while y == 'Y':
	print(color.yellow+'Is it a file or a folder???'+color.end)
	print(color.red+'0.\t'+color.green+'Exit'+color.end)
	print(color.red+'1.\t'+color.green+'File'+color.end)
	print(color.red+'2.\t'+color.green+'Folder'+color.end)
	ch = int(input(color.purple+'Enter your choice:\t'+color.end))
	if ch == 0:
		print(color.cyan+'Exiting........'+color.end)
		exit()
	if ch == 1:
		c = 'Y'
		while c == 'Y':
			path = input(color.darkcyan+'Enter path to file:\t'+color.end)
			print(color.purple+'Files in '+color.end,path,':-')
			os.chdir(path)
			subprocess.run(['ls'])
			c1 = input(color.darkcyan+'Do you want to continue removing file(Y/n):\t'+color.end)
			if c1 == 'Y':
				os.chdir(path)
				file1 = input(color.yellow+'Enter file name:\t'+color.end)
				subprocess.run(['sudo','rm','file1'])
			c = input(color.purple+'Do you want to continue removing files(Y/n):\t'+color.end)
	if ch == 2:
		c2 = 'Y'
		while c2 == 'Y':
			path1 = input(color.darkcyan+'Enter path to folder:\t'+color.end)
			print(color.purple+'Folders an files in'+color.end,path1,':-')
			os.chdir(path1)
			os.system('ls')
			c3 = input(color.darkcyan+'Do you want to continue(Y/n):\t'+color.end) 
			if c3 == 'Y':
				os.chdir(path1)
				folder = input(color.yellow+'Enter folder name:\t'+color.end)
				subprocess.run(['sudo','rm','-r',folder])
			c2 = input(color.purple+'Do you want to continue removing folder(Y/n):\t'+color.end)					
	y = input(color.orange+color.bold+'Do you want to continue removing files and folders(Y/n):\t'+color.end)
