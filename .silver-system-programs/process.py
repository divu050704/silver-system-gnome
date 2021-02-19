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
print(color.red+color.bold+'\t\tYour running processes are:\t'+color.yellow)
os.system('ps -ef')
c = input(color.green+'Do you want to kill any process(Y/n):\t')
if c == 'Y':
        pro= input(color.darkcyan+'Enter process id:\t')
        subprocess.run(['kill',pro])
