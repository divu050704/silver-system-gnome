import os 
#you can also use variable in subprocess but not in os library, but os library is useful for changing directories
import subprocess
#colors for better understanding
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
   print(color.red+'1.\t'+color.green+'File'+color.end)#There are different commands for files and folders
   print(color.red+'2\t'+color.green+'Folder'+color.end)
   k = int(input(color.purple+'Enter your choice:\t'+color.yellow))
   if k == 1:
      path = input(color.purple+'Enter path to parent directory:\t'+color.yellow)#Just till parent directory(Excluing name of file)
      os.chdir(path)
      print(color.red+'Files in',path+color.green)
      os.system('ls -p | grep -v /')# This will only show files in the directory
      file1= input(color.darkcyan+'Enter file name you want to copy:\t'+color.yellow)# Name of the file to copy
      target = input(color.purple+'Enter path to destination:\t'+color.yellow)#Path to the directory in which you want to copy the file 
      subprocess.run(['cp',file1,target])#main copy file 
      print(color.red+'Files in ',target+color.green)#just for satisfaction that the file has been copied in the directory
      os.chdir(target)#changing directory for python
      os.system('ls -p | grep -v /')#main command for confirmation
   if k == 2:
      path1 = input(color.purple+'Enter path to parent directory of folder:\t'+color.yellow)#Again just till the directory in which the folder exists
      os.chdir(path1)#changing path for the file 
      print(color.red+'Folders in',path1+color.green)#This will tell the folders in the directory
      os.system('ls -d */') # ls command which only show names ending with /(Directory)
      file2 = input(color.darkcyan+'Enter folder name you want to copy:\t'+color.yellow)
      target1= input(color.purple+'Enter path to destination:\t'+color.yellow)#Destination of the directory where you have to copy the file 
      subprocess.run(['cp','-r',file2,target1])#command for copying folders. (See the difference between file and folder, you have to add -r for folders)
      print(color.red+'Folders in',target1+color.green)#Just for checking that everythong has gone well
      os.chdir(target1)#changing working directory 
      os.system('ls -d */')#This will show only folders in the dirctory
   c = input(color.bold+color.blue+'Do you want to continue coping files(Y/n):\t'+color.end)#confirmation to restart the loop
