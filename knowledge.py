c = 'Y'
while c == 'Y':
	print('0.\t Exit')
	print('1.\t See boot time')
	print('2.\t System upgrade')
	print('3.\t Ping any website')
	print('4.\t Search devices connected to wifi')
	print('5.\t Install new application')
	print('6.\t Run an application')
	print('7.\t Remove an application')
	print('8.\t Change your working directory')
	print('9.\t To see files in a particular folder')
	print('10.\t To remove files and folders')
	ch = int(input('Enter your choice:\t'))
	if ch == 0:
		exit()
	if ch == 1:
		print('\nCode is:\t','$ systemd-analyze')	
		print('\nFor blame:\t','$ systemd-analyze blame')
		print('\nFor cahin:\t','$ systemd-analyze blame-chain')
	if ch == 2:
		print('\n$ sudo apt update && sudo apt lsit --upgradable -a')
		print('If upgrade:- $ sudo apt upgrade')
	if ch == 3:
		print('\n$ ping <website>')
	if ch == 4:
		print('\n$ sudo nmap -sn <ip-address of router>')
		print('ping <ip of device>')
	if ch == 5:
		p = 'Y'
		while p == 'Y':
			print('0.\t Exit')
			print('1.\t From apt')
			print('2.\t From snap')
			print('3.\t From software center')
			y = int(input('Enter you choice:\t'))
			if y == 0:
				exit()
			if y == 1:
				print('\nFirst:- $ sudo apt search <software>')
				print('Then:- $ sudo apt install <software>')
			if y == 2:
				print('\nFirst:- $ sudo snap search <software>')
				print('Then:- $ sudo snap install <software>')
			if y == 3:
				print('\n$ gnome-software')
			p = input('\nDo you want to continue search code for install(Y/n):\t')
	if ch == 6:
		c2 = 'Y'
		while c2 == 'Y':
			print('0.\t Exit')		
			print('1.\t Audacity')
			print('2.\t Blender')
			print('3.\t Calculator')
			print('4.\t Cheese')
			print('5.\t Files')
			print('6.\t Gedit text editor')
			print('7.\t Google Chrome')
			print('8.\t htop')
			print('9.\t Idle')
			print('10.\t LibreOffice')
			print('11.\t Microsoft Edge')
			print('12.\t Microsoft teams')
			print('13.\t Mozilla Firefox')
			print('14.\t Openshot')
			print('15.\t Rhythmbox')
			print('16.\t Settings')
			print('17.\t Smplayer')
			print('18.\t Telegram')
			print('19.\t Terminal')
			print('20.\t Tweak')
			print('21.\t VLC Player')
			print('22.\t Vim')
			print('23.\t Virtual Machines')
			print('24.\t Whatsapp')
			y1 = int(input('Enter you choice:\t'))
			if y1 == 1:
				print('\n$ auadcity')			
			if y1 == 2:
				print('\n$ blender')
			if y1 == 3:
				print('\n$ gnome-calculator')
			if y1 == 4:
				print('\n$ cheese')
			if y1 == 5:
				print('\n$ nautilus')
			if y1 == 6:
				print('\n$ gedit <path-to-file>')
			if y1 == 7:
				print('\n$ google-chrome')
			if y1 == 8:
				print('\n$ htop')
			if y1 == 9:
				print('\n$ idle <path-to-file>')
			if y1 == 10:
				y3 = 'Y'
				while y3 == 'Y':
					print('0.\t Exit')
					print('1.\t Documents')
					print('2.\t Excel')
					print('3.\t Powerpoint')
					print('4.\t One note')
					print('5.\t Libreoffice Math')
					ch1 = int(input('Enter your '))
					if ch1 == 0:
						exit()
					if ch1 == 1:
						print('\n$ libreoffice --writer') 
					if ch1 == 2:
						print('\n$ libreoffice --calc')
					if ch1 == 3:
						print('\n$ libreoffice --impress')
					if ch1 == 4:
						print('\n$ libreoffice --draw')
					if ch1 == 5:
						print('\n$ libreoffice --math')
					y3 = input('\nDo you want to continue opening LibreOffice(Y/n):\t')
			if y1 == 11:
				print('\n$ microsoft-edge')
			if y1 == 12:
				print('\n$ teams')
			if y1 == 13:
				print('\n$ firefox')
			if y1 == 14:
				print('\n$ openshot-qt')
			if y1 == 15:
				print('\n$ rhythmbox')
			if y1 == 16:
				print('\n$ gnome-control-center')
			if y1 == 17:
				print('\n$ smplayer')
			if y1 == 18:
				print('\n$ telegram-desktop')
			if y1 == 19:
				print('\n$ gnome-terminal')
			if y1 == 20:
				print('\n$ gnome-tweaks')
			if y1 == 21:
				print('\n$ /usr/bin/vlc')
			if y1 == 22:
				print('\n$ vim <path><file-name>')	
			if y1 == 23:
				print('\n$ VirtualBoxVM --startvm <name-of-virtual-machine>')
			if y1 == 24:
				print('\n$ google-chrome --app https://web.whatsapp.com')
			c2 = input('\nDo you want to continue serching codes for applications(Y/n):\t')
	if ch == 7:
		i = 'Y'
		while i == 'Y':
			print('Software:-')
			print('0.\t Exit')
			print('1.\t apt')
			print('2.\t snap')
			g = int(input('Enter your choics:\t'))
			if g == 0:
				exit()
			if g == 1:
				print('\n$ sudo apt remove <software>')
				print('if autoremove performed:\t$ sudo apt autoremove')
			if g == 2:
				print('\n$ sudo snap remove <software>')				
				print('If autoremove performed:\t$ sudo apt autoremove')
			i = input('\nDo you want to continue see code for remove of software:\t')
	if ch == 8:
		print('\n$ cd <path>')
	if ch == 9:
		print('\n$ ls <path-to-directory>')
	if ch == 10:
		k = 'Y'
		while k == 'Y':
			print('Type:-')
			print('1.\t File' )
			print('2.\t Folder')
			d = int(input('Enter your choice:\t'))
			if d == 1:
				print('\n$ sudo rm <path><file>')
			if d == 2:
				print('\n$ sudo rm -r <path><folder>')
			k = input('\nDo you want to continue see code for remove of files and folders(Y/n):\t')
	if ch == 11:
		print('\n$ mv <file-to-be-moved> <final-destination-of-file-or-folder>')
	if ch == 12:
		print('\n$ cp <file-to-be-copied> <final-destination-of-file-or-folder>')
	c = input('\nDo you want to continue looking for codes(Y/n):\t') 
