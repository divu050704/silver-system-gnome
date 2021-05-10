# This program contains all the  commands used for making this software
c = 'Y'
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

while c == 'Y':
	print(color.red+'0.\t'+color.green+'Exit'+color.end)
	print(color.red+'1.\t'+color.green+'See boot time'+color.end)
	print(color.red+'2.\t'+color.green+'Do a system upgrade'+color.end)
	print(color.red+'3.\t'+color.green+'Ping any website'+color.end)
	print(color.red+'4.\t'+color.green+'Search devices connected to wifi'+color.end)
	print(color.red+'5.\t'+color.green+'Install a new application'+color.end)
	print(color.red+'6.\t'+color.green+'Remove an application'+color.end)
	print(color.red+'7.\t'+color.green+'Change your working directory'+color.end)
	print(color.red+'8.\t'+color.green+'Want to see files in a particular folder'+color.end)
	print(color.red+'9.\t'+color.green+'Want to remove files and folders'+color.end)
	print(color.red+'10.\t'+color.green+'Move files and folders'+color.end)
	print(color.red+'11.\t'+color.green+'Copy files and folders'+color.end)
	print(color.red+'12.\t'+color.green+'Locate files and folders'+color.end)
	print(color.red+'13.\t'+color.green+'Search a keyword in a file'+color.end)
	print(color.red+'14.\t'+color.green+'Want to know about your machine'+color.end)
	print(color.red+'15.\t'+color.green+'Want to see disk information'+color.end)
	print(color.red+'16.\t'+color.green+'Rename a file'+color.end)
	print(color.red+'17.\t'+color.green+'Check running process and kill them'+color.end)
	print(color.red+'18.\t'+color.green+'Change permissions of a file'+color.end)
	print(color.red+'19.\t'+color.green+'Locate a specific type of file'+color.end)
	ch = float(input(color.purple+'Enter you choice:\t'+color.end))	
	if ch == 0:
		exit()
	if ch == 1:
		print(color.yellow+'\nCode is:\t',color.blued+'$ systemd-analyze'+color.end)#This will show only the time taken to boot up
		print(color.yellow+'\nFor blame:\t',color.blued+'$ systemd-analyze blame'+color.end)#This will show time with processes
		print(color.yellow+'\nFor chain:\t',color.blued+'$ systemd-analyze critical-chain'+color.end)#This will show processes in a chain form 
	if ch == 2:
		print(color.blued+'\n$ sudo apt update && sudo apt list --upgradable -a'+color.end)#'sudo apt update' will check whether there is any update for the package or not and 'sudo apt list --upgradable -a' will list all the packages that can be updated
		print(color.yellow+'If upgrade:-\t'+color.blued+'$ sudo apt upgrade'+color.end)# If their is any upgarde and the user wishes to upgrade then 'sudo apt upgrade' will be executed
	if ch == 3:
		print(color.blued+'\n$ ping -c 10 <website>'+color.end) # ping command will send empty data packets to the domain 10 times
	if ch == 4:
		print(color.blued+'\n$ sudo nmap -sn <ip-address of router>'+color.end)
		print(color.blued+'ping <ip of device>'+color.end)
	if ch == 5:
		p = 'Y'
		while p == 'Y':
			print(color.red+'0.\t'+color.green+'Exit'+color.end)
			print(color.red+'1.\t'+color.green+'Install from apt'+color.end)
			print(color.red+'2.\t'+color.green+'Install from snap'+color.end)
			print(color.red+'3.\t'+color.green+'Install from git'+color.end)
			print(color.red+'4.\t'+color.green+'Install from software center'+color.end)
			y = int(input(color.purple+'Enter choice:\t'+color.end))
			if y == 0:
				exit()
			if y == 1:
				print(color.yellow+'\nFirst:-\t'+color.blued+'$ sudo apt search <software>')#This wil first search whether the package in list of package manager or not and similar packages
				print(color.yellow+'Then:-\t'+color.blued+'$ sudo apt install <software>')#This will install the software
			if y == 2:
				print(color.yellow+'\nFirst:-\t'+color.blued+'$ sudo snap search <software>')#It will search whether the package exists or not on snap package manager's list and will show similar packages if the packages is not available
				print(color.blued+'Then:- $ sudo snap install <software>')#This will install the package
			if y == 3:
				print('\n$ gnome-software')#simply opens gnome-softare centre
			p = input(color.cyan+'\nDo you want to continue search code for install(Y/n):\t'+color.end)
	if ch == 6:
		i = 'Y'
		while i == 'Y':
			print('Software:-')
			print(color.red+'0.\t'+color.green+'Exit'+color.end)
			print(color.red+'1.\t'+color.green+'Installed from apt'+color.end)
			print(color.red+'2.\t'+color.green+'Installed from snap'+color.end)
			g = int(input(color.purple+'Enter your choics:\t'+color.end))
			if g == 0:
				print(color.cyan+'Exiting...............'+color.end)
				exit()
			if g == 1:
				print(color.blued+'\n$ sudo apt remove <software>'+color.end)#This will remove the package 
				print(color.yellow+'If autoremove performed:\t'+color.blued+'$ sudo apt autoremove'+color.end)#This will remove the packages dependent on the removed software and no longer required
			if g == 2:
				print(color.blued+'\n$ sudo snap remove <software>'+color.end)#This will remove the package from  the system
			i = input(color.purple+'\nDo you want to continue see code for remove of software:\t'+color.end)
	if ch == 7:
		print(color.blued+'\n$ cd <path>'+color.end)#cd stands for 'Change Directory"
	if ch == 8:
		print(color.blued+'\n$ ls <path-to-directory>'+color.end)#ls showas all the file s and folders in a particular directory 
	if ch == 9:
		k = 'Y'
		while k == 'Y':
			print(color.yellow+'Type:-'+color.end)
			print(color.red+'1.\t'+color.green+'File' +color.end)
			print(color.red+'2.\t'+color.green+'Folder'+color.end)
			d = int(input(color.purple+'Enter your choice:\t'+color.end))
			if d == 1:
				print(color.blue+'\n$ sudo rm <path><file>'+color.end)#We use only  rm to remove the file(sudo is used in case the file has root permissions)
			if d == 2:
				print(color.blue+'\n$ sudo rm -r <path><folder>'+color.end)#We also use rm -r to remove directories(sudo is used in case the folder has root permissions)
			k = input(color.purple+'\nDo you want to continue see code for remove of files and folders(Y/n):\t'+color.end)
	if ch == 10:
		print(color.blued+'\n$ mv <filename> <destination>'+color.end)#mv command files and directories to another directory and also creates a new directory if doesn't exist 		
	if ch == 11:
		print(color.red+'0.\t'+color.green+'Exit'+color.end)
		print(color.red+'1.\t'+color.green+'Files'+color.end)
		print(color.red+'2.\t'+color.green+'Folders'+color.end)
		k = int(input(color.purple+'Enter your choice:\t'+color.yellow))
		if k == 1:
			print(color.blued+'\n$ cp <filename> <target-directory>')#cp command only copy files and not directories
		if k == 2:
			print(color.blued+'\n$ cp -r <foldername> <target-directory>'+color.end)#use it with -r to move directories
	if ch == 12:
		print(color.blued+'\n$ locate <filename>')#locate is a package available on apt('sudo apt update && sudo apt upgrade && sudo apt install locate')
	if ch == 13:
		print(color.blued+'\n$ grep <keyword> <filename>')#grep is used in string manipulations in bash and there are many other uses of grep
	if ch == 14:
		print(color.blued+'\n$ neofetch ')#you need to install neofetch package before usage('sudo apt update && sudo apt upgrade && sudo apt install neofetch')
	if ch == 15:
		print(color.red+'0.\t'+color.green+'Exit'+color.end)
		print(color.red+'1.\t'+color.green+'Megabyte'+color.end)
		print(color.red+'2.\t'+color.green+'Bytes'+color.end)
		y = int(input(color.purple+'Enter your choice:\t'+color.yellow))
		if y == 1:
			print(color.blued+'\n$ df -m')#df -m prints disk partitions in megaytes
		if y == 2:
			print(color.blued+'\n$ df')
	if ch == 16:
		print(color.blued+'\n$ mv <old-filename> <new-filename>')#mv can also be used for renaming a file or a directory  
	if ch == 17:
		print(color.green+'\nChecking process:\t'+color.blued+'$ ps -ef'+color.end)#This will show all the running processes
		print(color.green+'If killed:\t'+color.blued+'kill <pid>'+color.end)# This will kill the process 
	if ch == 18:
		y = 'Y'
		while y == 'Y':
			print(color.red+'0.\t'+color.green+'Exit'+color.end)
			print(color.red+'1.\t'+color.green+'Change permission to read-only'+color.end)
			print(color.red+'2.\t'+color.green+'Change permission to write-only'+color.end)
			print(color.red+'3.\t'+color.green+'Change permission to read and write'+color.end)
			print(color.red+'4.\t'+color.green+'Change permission to execute-only'+color.end)
			print(color.red+'5.\t'+color.green+'Change permission to read, write and execute(Superuser)'+color.end)
			c = int(input(color.purple+'Enter your choice:\t'+color.yellow))
			if c == 1:
				print(color.blued+'\n$ chmod +r-w-x <filename>')#This will change the file permissions to read only
			if c == 2:
				print(color.blued+'\n$ chmod -r+w-x <filename>')#This will change the file permissions to write only
			if c == 3:
				print(color.blued+'\n$ chmod +r+w-x <filename>')#This will change the file permissions to read and write 
			if c == 4:
				print(color.blued+'\n$ chmod -r-w+x <filename>')#This will change file permissions to execution only
			if c == 5:
				print(color.blued+'\n$ chmod +r+w+x <filename>')#This will change the file permissions to read, write and exucute(superuser)
			y = input(color.cyan+'\nDo you want to cotinue seeing code for changing permissions(Y/n):\t'+color.yellow)		
	if ch == 19:
		print(color.blued+'\n$ locate *.<filetype>'+color.end)#locate is again used for searching a file with *. in place name of the file 
	c = input(color.darkcyan+color.bold+'\nDo you want to continue looking for codes(Y/n):\t'+color.yellow) 
