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
c = 'Y'
while c == "Y":
    path = input(color.purple+'Enter path to parent directory to the file:\t'+color.end)
    os.chdir(path)
    os.system('ls')
    file1 = input(color.darkcyan+'Enter file name you want to move:\t'+color.end)
    dest = input(color.purple+'Enter destination of file from root:\t'+color.end)
    subprocess.run(['mv',file1,dest])
    os.chdir(dest)
    print(color.red+'\nFile changed:-'+color.end)
    os.system('ls')
    c= input(color.bold+color.blue+'Do you want to continue moving file(Y/n):\t')
