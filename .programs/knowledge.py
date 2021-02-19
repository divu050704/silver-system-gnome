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
	print(color.red+'1.\t'+color.green+'See boot time'+color.end)
	print(color.red+'2.\t'+color.green+'Do a system upgrade'+color.end)
	print(color.red+'3.\t'+color.green+'Ping any website'+color.end)
	print(color.red+'4.\t'+color.green+'Search devices connected to wifi'+color.end)
	print(color.red+'5.\t'+color.green+'Install a new application'+color.end)
	print(color.red+'6.\t'+color.green+'Run an application'+color.end)
	print(color.red+'7.\t'+color.green+'Remove an application'+color.end)
	print(color.red+'8.\t'+color.green+'Change your working directory'+color.end)
	print(color.red+'9.\t'+color.green+'Want to see files in a particular folder'+color.end)
	print(color.red+'10.\t'+color.green+'Want to remove files and folders'+color.end)
	print(color.red+'11.\t'+color.green+'Move files and folders'+color.end)
	print(color.red+'12.\t'+color.green+'Copy files and folders'+color.end)
	print(color.red+'13.\t'+color.green+'Locate files and folders'+color.end)
	print(color.red+'14.\t'+color.green+'Search a keyword in a file'+color.end)
	print(color.red+'15.\t'+color.green+'Want to know about your machine'+color.end)
	print(color.red+'16.\t'+color.green+'Want to see disk information'+color.end)
	ch = float(input(color.purple+'Enter you choice:\t'+color.end))	
	if ch == 0:
		exit()
	if ch == 1:
		print(color.yellow+'\nCode is:\t',color.blued+'$ systemd-analyze'+color.end)	
		print(color.yellow+'\nFor blame:\t',color.blued+'$ systemd-analyze blame'+color.end)
		print(color.yellow+'\nFor cahin:\t',color.blued+'$ systemd-analyze critical-chain'+color.end)
	if ch == 2:
		print(color.blued+'\n$ sudo apt update && sudo apt lsit --upgradable -a'+color.end)
		print(color.yellow+'If upgrade:-\t'+color.blued+'$ sudo apt upgrade'+color.end)
	if ch == 3:
		print(color.blued+'\n$ ping <website>'+color.end)
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
			print(color.red+'4.\t'+color.green+'Instll from software center'+color.end)
			y = int(input(color.purple+'Enter choice:\t'+color.end))
			if y == 0:
				exit()
			if y == 1:
				print(color.yellow+'\nFirst:-\t'+color.blued+'$ sudo apt search <software>')
				print(color.yellow+'Then:-\t'+color.blued+'$ sudo apt install <software>')
			if y == 2:
				print(color.yellow+'\nFirst:-\t'+color.blued+'$ sudo snap search <software>')
				print(color.blued+'Then:- $ sudo snap install <software>')
			if y == 3:
				print('\n$ gnome-software')
			p = input(color.cyan+'\nDo you want to continue search code for install(Y/n):\t'+color.end)
	if ch == 6:
		c2 = 'Y'
		while c2 == 'Y':
			print(color.yellow+'Which application You want to open:'+color.end)
			print(color.red+'0.\t'+color.green+'Exit'+color.end)
			print(color.red+'1.\t'+color.green+'Audacity'+color.end)	
			print(color.red+'2.\t'+color.green+'Blender'+color.end)
			print(color.red+'3.\t'+color.green+'Calculator'+color.end)
			print(color.red+'4.\t'+color.green+'Cheese'+color.end)
			print(color.red+'5.\t'+color.green+'Files'+color.end)
			print(color.red+'6.\t'+color.green+'Gedit text editor'+color.end)
			print(color.red+'7.\t'+color.green+'Google Chrome'+color.end)
			print(color.red+'8.\t'+color.green+'htop'+color.end)
			print(color.red+'9.\t'+color.green+'Idle '+color.end)
			print(color.red+'10.\t'+color.green+'Libreoffice'+color.end)
			print(color.red+'11.\t'+color.green+'Microsoft Edge'+color.end)
			print(color.red+'12.\t'+color.green+'Microsoft Teams'+color.end)
			print(color.red+'13.\t'+color.green+'Mozilla Firefox'+color.end)
			print(color.red+'14.\t'+color.green+'Openshot'+color.end)
			print(color.red+'15.\t'+color.green+'Rhythmbox'+color.end)
			print(color.red+'16.\t'+color.green+'Settings'+color.end)
			print(color.red+'17.\t'+color.green+'Smplayer'+color.end)
			print(color.red+'18.\t'+color.green+'Telegram'+color.end)
			print(color.red+'19.\t'+color.green+'Terminal'+color.end)
			print(color.red+'20.\t'+color.green+'Tweak your ubuntu'+color.end)	
			print(color.red+'21.\t'+color.green+'VLC Player'+color.end)
			print(color.red+'22.\t'+color.green+'Vim'+color.end)
			print(color.red+'23.\t'+color.green+'Virtual Machines'+color.end)
			print(color.red+'24.\t'+color.green+'Whatsapp'+color.end)
			y1 = int(input(color.purple+'Enter you Choice:\t'+color.end))
			if y1 == 1:
				print(color.blued+'\n$ auadcity'+color.end)			
			if y1 == 2:
				print(color.blued+'\n$ blender'+color.end)
			if y1 == 3:
				print(color.blued+'\n$ gnome-calculator'+color.end)
			if y1 == 4:
				print(color.blued+'\n$ cheese'+color.end)
			if y1 == 5:
				print(color.blued+'\n$ nautilus'+color.end)
			if y1 == 6:
				print(color.blued+'\n$ gedit <path-to-file>'+color.end)
			if y1 == 7:
				print(color.blued+'\n$ google-chrome'+color.end)
			if y1 == 8:
				print(color.blued+'\n$ htop'+color.end)
			if y1 == 9:
				print(color.blued+'\n$ idle <path-to-file>'+color.end)
			if y1 == 10:
				y3 = 'Y'
				while y3 == 'Y':
					print(color.red+'0.\t'+color.green+'Exit'+color.end)
					print(color.red+'1.\t'+color.green+'Documents'+color.end)
					print(color.red+'2.\t'+color.green+'Excel'+color.end)
					print(color.red+'3.\t'+color.green+'Powerpoint'+color.end)
					print(color.red+'4.\t'+color.green+'One note'+color.end)
					print(color.red+'5.\t'+color.green+'Libreoffice Math'+color.end)
					ch1  = int(input(color.purple+'Enter your choice:\t'+color.end))
					if ch1 == 0:
						exit()
					if ch1 == 1:
						print(color.blued+'\n$ libreoffice --writer'+color.end) 
					if ch1 == 2:
						print(color.blued+'\n$ libreoffice --calc'+color.end)
					if ch1 == 3:
						print(color.blued+'\n$ libreoffice --impress'+color.end)
					if ch1 == 4:
						print(color.blued+'\n$ libreoffice --draw'+color.end)
					if ch1 == 5:
						print(color.blued+'\n$ libreoffice --math'+color.end)
					y3 = input(color.purple+'\nDo you want to continue opening LibreOffice(Y/n):\t'+color.end)
			if y1 == 11:
				print(color.blued+'\n$ microsoft-edge'+color.end)
			if y1 == 12:
				print(color.blued+'\n$ teams'+color.end)
			if y1 == 13:
				print(color.blued+'\n$ firefox'+color.end)
			if y1 == 14:
				print(color.blued+'\n$ openshot-qt'+color.end)
			if y1 == 15:
				print(color.blued+'\n$ rhythmbox'+color.end)
			if y1 == 16:
				print(color.blued+'\n$ gnome-control-center'+color.end)
			if y1 == 17:
				print(color.blued+'\n$ smplayer'+color.end)
			if y1 == 18:
				print(color.blued+'\n$ telegram-desktop'+color.end)
			if y1 == 19:
				print(color.blued+'\n$ gnome-terminal'+color.end)
			if y1 == 20:
				print(color.blued+'\n$ gnome-tweaks'+color.end)
			if y1 == 21:
				print(color.blued+'\n$ /usr/bin/vlc'+color.end)
			if y1 == 22:
				print(color.blued+'\n$ vim <path><file-name>'+color.end)	
			if y1 == 23:
				print(color.blued+'\n$ VirtualBoxVM --startvm <name-of-virtual-machine>'+color.end)
			if y1 == 24:
				print(color.blued+'\n$ google-chrome --app https://web.whatsapp.com'+color.end)
			c2 = input(color.purple+'\nDo you want to continue serching codes for applications(Y/n):\t'+color.end)
	if ch == 7:
		i = 'Y'
		while i == 'Y':
			print('Software:-')
			print(color.red+'0.\t'+color.green+'Exit'+color.end)
			print(color.red+'1.\t'+color.green+'Install from apt'+color.end)
			print(color.red+'2.\t'+color.green+'Install from snap'+color.end)
			print(color.red+'3.\t'+color.green+'Install from git'+color.end)
			print(color.red+'4.\t'+color.green+'Instll from software center'+color.end)
			g = int(input(color.purple+'Enter your choics:\t'+color.end))
			if g == 0:
				print(color.cyan+'Exiting...............'+color.end)
				exit()
			if g == 1:
				print(color.blued+'\n$ sudo apt remove <software>'+color.end)
				print(color.yellow+'If autoremove performed:\t'+color.blued+'$ sudo apt autoremove'+color.end)
			if g == 2:
				print(color.blued+'\n$ sudo snap remove <software>'+color.end)				
				print(color.yellow+'If autoremove performed:\t'+color.blued+'$ sudo apt autoremove'+color.end)
			i = input(color.purple+'\nDo you want to continue see code for remove of software:\t'+color.end)
	if ch == 8:
		print(color.blued+'\n$ cd <path>'+color.end)
	if ch == 9:
		print(color.blued+'\n$ ls <path-to-directory>'+color.end)
	if ch == 10:
		k = 'Y'
		while k == 'Y':
			print(color.yellow+'Type:-'+color.end)
			print(color.red+'1.\t'+color.green+'File' +color.end)
			print(color.red+'2.\t'+color.green+'Folder'+color.end)
			d = int(input(color.purple+'Enter your choice:\t'+color.end))
			if d == 1:
				print(color.blue+'\n$ sudo rm <path><file>'+color.end)
			if d == 2:
				print(color.blue+'\n$ sudo rm -r <path><folder>'+color.end)
			k = input(color.purple+'\nDo you want to continue see code for remove of files and folders(Y/n):\t'+color.end)
	c = input(color.darkcyan+color.bold+'\nDo you want to continue looking for codes(Y/n):\t'+color.end) 
