import os
import subprocess
class color:
   purple = '\033[95m'
   cyan = '\033[96m'
   darkcyan = '\033[36m'
   blue = '\033[94m'
   green = '\033[92m'
   yellow = '\033[93m'
   red = '\033[91m'
   silver = '\033[3;30;47m'
   bold = '\033[1m'
   underline = '\033[4m'
   end = '\033[0m'
ch = 'Y'
def zero():
	exit()
def zero1():
	os.system('python3 count.py')
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
def sixteen():
	os.system('python3 disk-info.py')

if ch == 'n':
	exit()
while ch == 'Y':
	print(color.bold+color.silver+'\t\t                  UUUUUUUUUU            '+color.end)
	print(color.bold+color.silver+'\t\t            UUUUUU|UUU                  '+color.end)
	print(color.bold+color.silver+'\t\t            |     |                     '+color.end)
	print(color.bold+color.silver+'\t\t            |      UUUUUUUUUU           '+color.end)
	print(color.bold+color.silver+'\t\t             UUUUUUUUU     |            '+color.end)
	print(color.bold+color.silver+'\t\t                     |     |            '+color.end)
	print(color.bold+color.silver+'\t\t                   UU|UUUUUU            '+color.end)
	print(color.bold+color.silver+'\t\t             UUUUUUUUUU                 '+color.end)
	print(color.green+'0.\t Exit'+color.end)
	print(color.green+'0.1\t See number of lines in programs'+color.end)
	print(color.green+'0.2\t Want to see code for below programs'+color.end)
	print(color.green+'1.\t See boot time'+color.end)
	print(color.green+'2.\t Do a system upgrade'+color.end)
	print(color.green+'3.\t Ping any website'+color.end)
	print(color.green+'4.\t Search devices connected to wifi'+color.end)
	print(color.green+'5.\t Install a new application'+color.end)
	print(color.green+'6.\t Run an application'+color.end)
	print(color.green+'7.\t Remove an application'+color.end)
	print(color.green+'8.\t Change your working directory'+color.end)
	print(color.green+'9.\t Want to see files in a particular folder'+color.end)
	print(color.green+'10.\t Want to remove files and folders'+color.end)
	print(color.green+'11.\t Move files and folders'+color.end)
	print(color.green+'12.\t Copy files and folders'+color.end)
	print(color.green+'13.\t Locate files and folders'+color.end)
	print(color.green+'14.\t Search a keyword in a file'+color.end)
	print(color.green+'15.\t Want to know about your machine'+color.end)
	print(color.green+'16.\t Want to see disk information'+color.end)
	y = float(input(color.purple+'Enter you choice:\t'+color.end))		 
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
