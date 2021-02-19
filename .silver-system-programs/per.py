import os 
import subprocess
ch = 'Y'
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
   end = '\033[0'
if ch == 'n':
   exit()
while ch == 'Y':
   print(color.red+'0.\t'+color.green+'Exit'+color.end)
   print(color.red+'1.\t'+color.green+'Change permission to read-only'+color.end)
   print(color.red+'2.\t'+color.green+'Change permission to write-only'+color.end)
   print(color.red+'3.\t'+color.green+'Change permission to read and write'+color.end)
   print(color.red+'4.\t'+color.green+'Change permission to execute-only'+color.end)
   print(color.red+'5.\t'+color.green+'Change permission to read, write and execute(Superuser)'+color.end)
   y = int(input(color.purple+'Enter your choice:\t'+color.darkcyan))
   if y == 0:
      exit()
   if y == 1:
      path = (input('Enter parent directory of file:\t'))
      os.chdir(path)
      print(color.red+'Files in',path+color.yellow)
      os.system('ls')
      file1 = input(color.purple+'Enter file name:\t'+color.darkcyan)
      subprocess.run(['chmod','+r-w-x',file1])
      print(color.red+'Permission Changed to read only'+color.end)
   if y == 2:
      path1 = input(color.purple+'Enter path to parent directory of file:\t'+color.darkcyan)
      os.chdir(path1)
      print(color.red+'Files in',path1+color.yellow)
      os.system('ls')
      file2 = input(color.purple+'Enter file name:\t'+color.darkcyan)
      subprocess.run(['chmod','-r+w-x',file2])
      print(color.red+'Permission changed to write-only'+color.end)
   if y == 3:
      path2 = input('Enter path to parent directory of file:\t')
      os.chdir(path2)
      print(color.red+'Files in',path2+color.yellow)
      os.system('ls')
      file3 = input(color.purple+'Enter file name:\t'+color.darkcyan)
      subprocess.run(['chmod','+r+w-x',file3])
      print(color.red+'Permission changed to read and write both'+color.end)
   if y == 4:
      path3 = input(color.purple+'Enter path to parent directory of file:\t'+color.darkcyan)
      os.chdir(path3)
      print(color.red+'Files in',path3+color.yellow)
      os.system('ls')
      file4 = input(color.purple+'Enter file name:\t'+color.darkcyan)
      subprocess.run(['chmod','-r-w+x'])
      print(color.red+'Permission changed to execute-only')
   if y == 5:
      path4 = input(color.purple+'Enter path to parent folder of file:\t'+color.darkcyan)
      os.chdir(path4)
      print(color.red+'Files in:\t',path4+color.yellow)
      os.system('ls')
      file5 = input(color.purple+'Enter file name:\t'+color.darkcyan)
      subprocess.run(['chmod','+r+w+x',file5])
      print(color.red+'Permission Changed to read, wrie and execute'+color.end)
   ch = input(color.green+color.bold+'Do you want to continue changing permissions(Y/n):\t'+color.darkcyan)

   

	
