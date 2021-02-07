import os
import subprocess
ch = 'Y'
def zero():
	exit()
def zero1():
	print(282)
def zero2():
	os.system('python3 knowledge.py')
def one():
	
	os.system('python3 boot.py')
def two():
	
	os.system('python3 do.py')
def three():
	
	os.system('python3 ping.py')
def four():
	
	os.system('python3 wifi.py')
def five():
	
	os.system('python3 install.py')
def six():
	
	os.system('python3 app.py')
def seven():
	
	os.system('python3 remove.py')
def eight():
	
	os.system('python3 dir.py')
def nine():
	
	os.system('python3 file.py')
def ten():
	os.system('python3 del.py')
def eleven():
	os.system('python3 move.py')
def twelve():
	os.system('python3 copy.py')
def thirteen():
	os.system('python3 locate.py')
def fourteen():
	os.system('python3 search.py')
def fifteen():
	os.system('python3 about.py')
def sixteen()():
	os.system('python3 disk-info.py')
if ch == 'n':
	exit()
while ch == 'Y':
	print('0.\t Exit')
	print('0.1\t See number of lines in programs')
	print('0.2\t Want to see bash codes for following programs')
	print('1.\t See boot time')
	print('2.\t Do a system upgrade')
	print('3.\t Ping any website')
	print('4.\t Search devices connected to wifi')
	print('5.\t Install a new application')
	print('6.\t Run an application')
	print('7.\t Remove an application')
	print('8.\t Change your working directory')
	print('9.\t Want to see files in a particular folder')
	print('10.\t Want to remove files and folders')
	print('11.\t Move a file or folder')
	print('12.\t Copy foldes and files from one place to another')
	print('13.\t Locate files and folders')
	print('14.\t Search a keyword in a file')
	print('15.\t Want to know about your machine')
	print('16.\t Wnant to see disk information')
	y = float(input('Enter you choice:\t'))		 
	if y == 0 :
		zero()
	if y == 0.1:
		zero1()
	if y == 0.2:
		zero2()
	if y==1:
		one()
	if y==2:
		two()
	if y==3:
		three()
	if y==4:
		four()
	if y == 5:
		five()
	if y == 6:
		six()
	if y == 7:
		seven()
	if y == 8:
		eight()
	if y == 9:
		nine()
	if y == 10:
		ten()
	if y == 11:
		eleven()
	if y == 12:
		twelve()
	if y == 13:
		thirteen()
	if y == 14:
		fourteen()
	if y == 15:
		fifteen()
	if y == 16:
		sixteen()
	ch = input('\nDo you want to continue main program(Y/n):\t')
