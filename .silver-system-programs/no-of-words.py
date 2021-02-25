# Program to find no. of words in all the programs
file1 = open('/usr/.silver-system-programs/about.py','rt')
data1 = file1.read()
words1 = data1.split()
final1 = len(words1)
########################################################

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


#######################################################
file2 = open('/usr/.silver-system-programs/app.py','rt')
data2 = file2.read()
words2 = data1.split()
final2 = len(words2)
#######################################################
file3 = open('/usr/.silver-system-programs/boot.py','rt')

data3 = file3.read()
words3 = data1.split()
final3 = len(words3)
##############################################################
file4 = open('/usr/.silver-system-programs/copy.py','rt')

data4 = file4.read()
words4 = data4.split()
final4 = len(words4)
############################################################
file5 = open('/usr/.silver-system-programs/del.py','rt')

data5 = file5.read()
words5 = data5.split()
final5 = len(words5)
###########################################################
file6 = open('/usr/.silver-system-programs/dir.py','rt')
data6 = file6.read()
words6 = data6.split()
final6 = len(words6)
############################################################
file7 = open('/usr/.silver-system-programs/disk-info.py','rt')
data7 = file7.read()
words7 = data7.split()
final7 = len(words7)
##############################################################
file8 = open('/usr/.silver-system-programs/do.py','rt')
data8 = file8.read()
words8 = data8.split()
final8 = len(words8)

#################################################################
file9 = open('/usr/.silver-system-programs/file.py','rt')
data9 = file9.read()
words9 = data9.split()
final9 = len(words9)
#######################################################
file10 = open('/usr/.silver-system-programs/install.py','rt')
data10 = file10.read()
words10 = data10.split()
final10 = len(words10)
#########################################################
file11 = open('/usr/.silver-system-programs/knowledge.py','rt')
data11 = file11.read()
words11= data11.split()
final11 = len(words11)
##########################################################
file12 = open('/usr/.silver-system-programs/locate.py','rt')
data12 = file12.read()
words12 = data12.split()
final12 = len(words12) 
################################################################
file13 = open('/usr/.silver-system-programs/move.py','rt')
data13 = file13.read()
words13 = data13.split()
final13 = len(words13)
#############################################################
file14 = open('/usr/.silver-system-programs/ping.py','rt')
data14 = file14.read()
words14 = data14.split()
final14 = len(words14)
################################################################
file15 = open('/usr/.silver-system-programs/remove.py','rt')
data15 = file15.read()
words15 = data15.split()
final15 = len(words15)
###############################################################
file16 = open('/usr/.silver-system-programs/search.py','rt')
data16 = file16.read()
words16 = data16.split()
final16 = len(words16)
##############################################################
file17 = open('/usr/.silver-system-programs/wifi.py','rt')
data17 = file17.read()
words17 = data17.split()
final17 = len(words17)
###############################################################
file18 = open('/usr/.silver-system-programs/.oof.py','rt')
data18 = file18.read()
words18 = data18.split()
final18 = len(words18)
###############################################################
file19 = open('/usr/.silver-system-programs/count.py','rt')
data19 = file19.read()
words19 = data19.split()
final19 = len(words19)
################################################################
file20 = open('/usr/.silver-system-programs/per.py','rt')
data20 = file20.read()
words20 = data20.split()
final20 = len(words20)
###################################################################
file21 = open('/usr/.silver-system-programs/process.py','rt')
data21 = file21.read()
words21 = data21.split()
final21 = len(words21)
####################################################################
file22 = open('/usr/.silver-system-programs/nmap.sh','rt')
data22 = file22.read()
words22= data22.split()
final22 = len(words22)
#####################################################################
file23 = open('/usr/.silver-system-programs/main.sh')
data23 = file23.read()
words23 = data23.split()
final23 = len(words23)
#####################################################################
file24 = open('/usr/share/applications/silver-system.desktop','rt')
data24 = file24.read()
words24  = data24.split()
final24 = len(words24)
total = final1+final2+final3+final4+final5+final6+final7+final8+final9+final11+final12+final13+final14+final15+final16+final17+final18+final19+final20+final21+final22+final23+final24
total1 = total + 384 # Added for this file also
print(color.red+color.bold+'\nTotal number of words in all the programs:\t'+color.end,total1)
print()