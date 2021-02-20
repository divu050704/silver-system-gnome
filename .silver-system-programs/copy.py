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
   orange= '\033[33m'
   bold = '\033[1m'
   green = '\033[32m'
   underline = '\033[4m'
   end = '\033[0m'
c = 'Y'
while c == "Y":
   print(color.red+'0.\t'+color.green+'Exit'+color.end)
   print(color.red+'1.\t'+color.green+'File'+color.end)
   print(color.red+'2\t'+color.green+'Folder'+color.end)
   k = int(input(color.purple+'Enter your choice:\t'+color.yellow))
   if k == 1:
      path = input(color.purple+'Enter path to parent directory:\t'+color.yellow)
      os.chdir(path)
      print(color.red+'Files in',path+color.green)
      os.system('ls -p | grep -v /')
      file1= input(color.darkcyan+'Enter file name you want to copy:\t'+color.yellow)
      target = input(color.purple+'Enter path to destination:\t'+color.yellow)
      subprocess.run(['cp',file1,target])
      print(color.red+'Files in ',target+color.green)
      os.chdir(target)
      os.system('ls -p | grep -v /')
   if k == 2:
      path1 = input(color.purple+'Enter path to parent directory of folder:\t'+color.yellow)
      os.chdir(path1)
      print(color.red+'Folders in',path1+color.green)
      os.system('ls -d */')
      file2 = input(color.darkcyan+'Enter folder name you want to copy:\t'+color.yellow)
      target1= input(color.purple+'Enter path to destination:\t'+color.yellow)
      subprocess.run(['cp','-r',file2,target1])
      print(color.red+'Folders in',target1+color.green)
      os.chdir(target1)
      os.system('ls -d */')
   c = input(color.bold+color.blue+'Do you want to continue coping files(Y/n):\t'+color.end) 
	
