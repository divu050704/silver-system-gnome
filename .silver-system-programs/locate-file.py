from typing import Collection
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
c = 'Y'
while c == 'Y':
    file1 = input(color.purple+'Enter file extention you want to search:\t'+color.yellow)
    print(color.blued)
    search = subprocess.run(['locate','*.'+file1])
    c = input(color.purple+'Do you want to continue to locate files(Y/n):\t'+color.yellow)
