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
ch = 'Y'
while ch == 'Y':
	file2 = input(color.purple+'Enter file name you want to serch:\t'+color.end) 
	subprocess.run(['locate',file2])
	ch = input(color.bold+color.blue+'Do you want to continue searching for files(Y/n):\t'+color.end)
