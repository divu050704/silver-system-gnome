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
	print(color.yellow+'Is it a file or a folder???'+color.end)#Like copying the command for files and folders is different so an option for files and folders 
	print(color.red+'0.\t'+color.green+'Exit'+color.end)
	print(color.red+'1.\t'+color.green+'File'+color.end)
	print(color.red+'2.\t'+color.green+'Folder'+color.end)
	ch = int(input(color.purple+'Enter your choice:\t'+color.end))
	if ch == 0:#If person chooses to leave
		print(color.cyan+'Exiting........'+color.end)#Just to make it look better
		exit()
	if ch == 1:#If person chooses file 
		c = 'Y'#This only work one time in the loop and will follow the input in last of this while loop
		while c == 'Y':
			path = input(color.darkcyan+'Enter path to file:\t'+color.green)#Path to the file till parent directory only (excluding name of the file) 
			print(color.purple+'Files in ',path,':-'+color.yellow)#This will show the files in parent directory for choosing files
			os.chdir(path)#Change the working directory 
			subprocess.run(['ls'])
			c1 = input(color.darkcyan+'Do you want to continue removing file(Y/n):\t'+color.green)#One final confirmation so that you don't delete the wrong file 
			if c1 == 'Y':
				os.chdir(path)
				file1 = input(color.yellow+'Enter file name:\t'+color.green)#File name user want to delete
				subprocess.run(['sudo','rm',file1])#command for removing file from the system
			c = input(color.purple+'Do you want to continue removing files(Y/n):\t'+color.green)
	if ch == 2:
		c2 = 'Y'
		while c2 == 'Y':
                    path1 = input(color.darkcyan+'Enter path to folder:\t'+color.green)#Path till parent directory only
			print(color.purple+'Folders an files in',path1,':-'+color.yellow)#This will shoe the folders in the directory so that a person can choose the folder easily and need not to again and again remember the name of the folder
			os.chdir(path1)
			os.system('ls')
			c3 = input(color.darkcyan+'Do you want to continue(Y/n):\t'+color.end)#Final confirmation
			if c3 == 'Y':
				os.chdir(path1)
				folder = input(color.yellow+'Enter folder name:\t'+color.green)#folder name 
				subprocess.run(['sudo','rm','-r',folder])#You can see the difference between the commands used for removing file(rm) and folders(rm -r)
			c2 = input(color.purple+'Do you want to continue removing folder(Y/n):\t'+color.green)#Just in case someone need to repeat the procedure					
	y = input(color.blue+color.bold+'Do you want to continue removing files and folders(Y/n):\t'+color.green)
