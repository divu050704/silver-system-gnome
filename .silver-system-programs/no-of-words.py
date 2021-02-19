# Program to find no. of words in all the programs
file1 = open('about.py','rt')
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
file2 = open('app.py','rt')
data2 = file2.read()
words2 = data1.split()
final2 = len(words2)
#######################################################
file3 = open('boot.py','rt')

data3 = file3.read()
words3 = data1.split()
final3 = len(words3)
##############################################################
file4 = open('copy.py','rt')

data4 = file4.read()
words4 = data4.split()
final4 = len(words4)
############################################################
file5 = open('del.py','rt')

data5 = file5.read()
words5 = data5.split()
final5 = len(words5)
###########################################################
file6 = open('dir.py','rt')
data6 = file6.read()
words6 = data6.split()
final6 = len(words6)
############################################################
file7 = open('disk-info.py','rt')
data7 = file7.read()
words7 = data7.split()
final7 = len(words7)
##############################################################
file8 = open('do.py','rt')
data8 = file8.read()
words8 = data8.split()
final8 = len(words8)

#################################################################
file9 = open('file.py','rt')
data9 = file9.read()
words9 = data9.split()
final9 = len(words9)

 
#######################################################
file10 = open('install.py','rt')
data10 = file10.read()
words10 = data10.split()
final10 = len(words10)
#########################################################
file11 = open('knowledge.py','rt')
data11 = file11.read()
words11= data11.split()
final11 = len(words11)
##########################################################
file12 = open('locate.py','rt')
data12 = file12.read()
words12 = data12.split()
final12 = len(words12) 
################################################################
file13 = open('move.py','rt')
data13 = file13.read()
words13 = data13.split()
final13 = len(words13)
#############################################################
file14 = open('ping.py','rt')
data14 = file14.read()
words14 = data14.split()
final14 = len(words14)
################################################################
file15 = open('remove.py','rt')
data15 = file15.read()
words15 = data15.split()
final15 = len(words15)
###############################################################
file16 = open('search.py','rt')
data16 = file16.read()
words16 = data16.split()
final16 = len(words16)
##############################################################
file17 = open('wifi.py','rt')
data17 = file17.read()
words17 = data17.split()
final17 = len(words17)
###############################################################
file18 = open('.oof.py','rt')
data18 = file18.read()
words18 = data18.split()
final18 = len(words18)
###############################################################
file19 = open('count.py','rt')
data19 = file19.read()
words19 = data19.split()
final19 = len(words19)
################################################################
file20 = open('per.py','rt')
data20 = file20.read()
words20 = data20.split()
final20 = len(words20)
total = final1+final2+final3+final4+final5+final6+final7+final8+final9+final11+final12+final13+final14+final15+final16+final17+final18+final19+final20
total1 = total + 304 # Added for this file also
print(color.red+color.bold+'\nTotal number of words in all the programs:\t'+color.end,total1)
