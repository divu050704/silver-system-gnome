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
cmd = os.system('sudo apt update && sudo apt  list --upgradable -a')#This command will see if there are any updates for the system or not and if there are some updates then it list those upgrades
ch = input(color.purple+'Do you want to upgrade(Y/n):\t'+color.end)# confirmation if the user wants to do it right now or later 
if ch == 'Y':
	cmd2 = os.system('sudo apt upgrade')#If the user is ready for system upgarde then this command will be executed
else:
	print(color.cyan+'Exiting...............'+color.end)
	exit()
