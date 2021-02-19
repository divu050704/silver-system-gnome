import os
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
def zero():
	print('\nExiting..........')
	exit()
def zero1():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 count.py')
def zero2():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 knowledge.py')
def zero3():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 no-of-words.py')
def one():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 boot.py')
def two():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 do.py')
def three():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 ping.py')
def four():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 wifi.py')
def five():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 install.py')
def six():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 app.py')
def seven():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 remove.py')
def eight():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 dir.py')
def nine():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 file.py')
def ten():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 del.py')
def eleven():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 move.py')
def twelve():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 copy.py')
def thirteen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 locate.py')
def fourteen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 search.py')
def fifteen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 about.py')
def sixteen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 disk-info.py')
def seventeen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 rename.py')
def eighteen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 process.py')
def nineteen():
	os.chdir('/usr/.silver-system-programs')
	os.system('python3 per.py')
if ch == 'n':
	exit()
while ch == 'Y':
	print(color.bold+color.cyan+'\t\t\t                  UUUUUUUUUU            '+color.end)
	print(color.bold+color.cyan+'\t\t\t            UUUUUU|UUU                  '+color.end)
	print(color.bold+color.cyan+'\t\t\t            |     |                     '+color.end)
	print(color.bold+color.cyan+'\t\t\t            |      UUUUUUUUUU           '+color.end)
	print(color.bold+color.cyan+'\t\t\t             UUUUUUUUU     |            '+color.end)
	print(color.bold+color.cyan+'\t\t\t                     |     |            '+color.end)
	print(color.bold+color.cyan+'\t\t\t                   UU|UUUUUU            '+color.end)
	print(color.bold+color.cyan+'\t\t\t             UUUUUUUUUU                 '+color.end)
	print(color.red+'0.\t'+color.green+'Exit'+color.end)
	print(color.red+'0.1\t'+color.green+'See number of lines in programs'+color.end)
	print(color.red+'0.2\t'+color.green+'Want to see code for below programs'+color.end)
	print(color.red+'0.3\t'+color.green+'Want to see number of words in the following programs'+color.end)
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
	print(color.red+'17.\t'+color.green+'Rename a file'+color.end)
	print(color.red+'18.\t'+color.green+'Check running process and kill them'+color.end)
	print(color.red+'19.\t'+color.green+'Change permissions of a file'+color.end)
	y = float(input(color.purple+'Enter you choice:\t'+color.red))		 
	if y == 0 :
		zero()
	if y == 0.1:
		zero1()
	if y == 0.2:
		zero2()
	if y == 0.3:
		zero3()
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
	if y == 17:
		seventeen()
	if y == 18:
		eighteen()
	if y == 19:
		nineteen()
	ch = input(color.yellow+color.bold+'\nDo you want to continue main program(Y/n):\t'+color.orange)