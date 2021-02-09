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
def n1():
	os.system('audacity')
def n2():
	os.system('blender')
def n3():
	os.system('gnome-calculator')
def n4():
	os.system('cheese')
def n5():
	os.system('nautilus --new-window')
def n6():
	path  = input(color.purple+'Enter path to open file:\t'+color.end)
	os.chdir(path)
	file1 =  input(color.purple+'Enter file name:\t'+color.end)
	run =  subprocess.run(['gedit',file1])
def n7():
	os.system('google-chrome')
def n8():
	os.system('htop')
def n9():
	path = input(color.purple+'Enter the path where you want to save file:\t'+color.end)
	os.chdir(path)
	file1= input(color.purple+'Enter the filename you want to save:\t'+color.end)
	subprocess.run(['idle',file1])
def n10():
	c = 'Y'
	while c == 'Y':
		print(color.red+'0.\t'+color.green+'Exit'+color.end)
		print(color.red+'1.\t'+color.green+'Documents'+color.end)
		print(color.red+'2.\t'+color.green+'Excel'+color.end)
		print(color.red+'3.\t'+color.green+'Powerpoint'+color.end)
		print(color.red+'4.\t'+color.green+'One note'+color.end)
		print(color.red+'5.\t'+color.green+'Libreoffice Math'+color.end)
		y1  = int(input(color.purple+'Enter your choice:\t'+color.end))
		if y1 == 1:
			os.system('libreoffice --writer')
		if y1 == 2:
			os.system('libreoffice --calc')
		if y1 == 3:
			os.system('libreoffice --impress')
		if y1 == 4:
			os.system('libreoffice --draw')
		if y1 == 5:
			os.system('libreoffice --math')
		c= input(color.blue+'Do you want to continue opening applications in Libreoffice(Y/n):\t'+color.end)
	os.system('microsoft-edge')
def n12():
	os.system('teams')
def n13():
	os.system('firefox')
def n14():
	os.system('openshot-qt')
def n15():
	os.system('rhythmbox')
def n16():
	os.system('gnome-control-center')
def n17():
	os.system('smplayer')
def n18():
	os.system('telegram-desktop')
def n19():
	os.system('gnome-terminal')
def n20():
	os.system('gnome-tweaks')
def n21():
	os.system('/usr/bin/vlc --started-from-file')
def n22():
	path = input(color.red+'Enter path to save file:\t'+color.end)
	os.chdir(path)
	file1 = input(color.purple+'Enter file name to save:\t'+color.end)
	subprocess.run(['vim',file1])
def n23():
c2 = 'Y'
	while c2 == 'Y':
		print(color.yellow+'Which Virtual machine you want to run\t'+color.end)
		print(color.red+'1.\t'+color.green+'Lubuntu'+color.end)
		c3 = int(input(color.purple+'Enter your choice:\t'+color.end))
		if c3 == 1:
			os.system('VirtualBoxVM --startvm Lubuntu')
		c2 = input(color.blue+'Do you want to continue running Virtual Machines(Y/n):\t'+color.end)
def n24():
	os.system('google-chrome --app=https://web.whatsapp.com/')
#You can edit these applications as you want 
ch = 'Y'
while ch == 'Y':
	print('Which application You want to open:')
	print('0.\t Exit')
	print('1.\t Audacity')	
	print('2.\t Blender')
	print('3.\t Calculator')
	print('4.\t Cheese')
	print('5.\t Files')
	print('6.\t Gedit text editor')
	print('7.\t Google Chrome')
	print('8.\t htop')
	print('9.\t Idle ')
	print('10.\t Libreoffice')
	print('11.\t Microsoft Edge')
	print('12.\t Microsoft Teams')
	print('13.\t Mozilla Firefox')
	print('14.\t Openshot')
	print('15.\t Rhythmbox')
	print('16.\t Settings')
	print('17.\t Smplayer')
	print('18.\t Telegram')
	print('19.\t Terminal')
	print('20.\t Tweak your ubuntu')	
	print('21.\t VLC Player')
	print('22.\t Vim')
	print('23.\t Virtual Machines')
	print('24.\t Whatsapp')
	y = int(input('Enter you Choice:\t'))
	if y == 0:
		exit()
	if y == 1:
		n1()
	if y == 2:
		n2()
	if y == 3:
		n3()
	if y == 4:
		n4()
	if y == 5:
		n5()
	if y == 6:
		n6()
	if y == 7:
		n7()
	if y==8:
		n8()
	if y == 9:
		n9()
	if y == 10:
		n10()
	if y == 11 :
		n11()
	if y == 12:
		n12()
	if y == 13:
		n13()
	if y == 14:
		n14()
	if y == 15:
		n15()
	if y == 16:
		n16()
	if y == 17:
		n17()
	if y == 18:
		n18()
	if y == 19:
		n19()
	if y == 20 :
		n20()
	if y == 21:
		n21()
	if y == 22:
		n22()
	if y == 23:
		n23()
	if y == 24:
		n24()
	ch = input(color.orange+color.bold+'Do you want to continue opening applications(Y/n):\t'+color.end)
