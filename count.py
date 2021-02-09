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
file1 = open('about.py','r')
counter1 = 0
content1 = file1.read()
colist1 = content1.split('\n')
for i in colist1:
	if i:
 		counter1+=1
#######################################################
file2 = open('app.py','r')
counter2 = 0
content2 = file2.read()
colist2 = content2.split('\n')
for i in colist2:
	if i:
		counter2 += 1
#######################################################
file3 = open('boot.py','r')
counter3 = 0
content3 = file3.read()
colist3  = content3.split('\n')
for i in colist3:
	if i:
		counter3 += 1
##############################################################
file4 = open('copy.py','r')
counter4 = 0
content4 = file4.read()
colist4 = content4.split()
for i in colist4:
	if i:
		counter4+=1
############################################################
file5 = open('del.py','r')
counter5 = 0
content5 = file5.read()
colist5 = content5.split('\n')
for i in colist5:
	if i:
		counter5 += 1
###########################################################
file6 = open('dir.py','r')
counter6 = 0
content6 = file6.read()
colist6 = content6.split('\n')
for i in colist6:
	if i:
		counter6 += 1
############################################################
file7 = open('disk-info.py','r')
counter7 = 0
content7 = file7.read()
colist7 = content7.split('\n')
for i in colist7:
	if i:
		counter7 += 1
##############################################################
file8 = open('do.py','r')
counter8 = 0
content8 = file8.read()
colist8 = content8.split('\n')
for i in colist8:
	if i:
		counter8 += 1
#################################################################
file9 = open('file.py','r')
counter9 = 0
content9 = file9.read()
colist9 = content9.split('\n')
for i in colist9:
	if i:
		counter9 += 1
#############################################################

#######################################################
file11 = open('install.py','r')
counter11 = 0
content11 = file11.read()
colist11 = content11.split('\n')
for i in colist11:
	if i:
		counter11 += 1
#########################################################
file12 = open('knowledge.py','r')
counter12 = 0
content12 = file12.read()
colist12 = content12.split('\n')
for i in colist12:
	if i:
		counter12 += 1
##########################################################
file13 = open('locate.py','r')
counter13 = 0
content13 = file13.read()
colist13 = content13.split('\n')
for i in colist13:
	if i:
		counter13 += 1
################################################################
file14 = open('move.py','r')
counter14 = 0
content14 = file14.read()
colist14 = content14.split('\n')
for i in colist14:
	if i:
		counter14 += 1
#############################################################
file15 = open('ping.py','r')
counter15 = 0
content15 = file15.read()
colist15 = content15.split('\n')
for i in colist15:
	if i:
		counter15 += 1
################################################################
file16 = open('remove.py','r')
counter16 = 0
content16 = file16.read()
colist16 = content16.split('\n')
for i in colist16:
	if i:
		counter16 += 1
###############################################################
file17 = open('search.py','r')
counter17 = 0
content17 = file17.read()
colist17 = content17.split('\n')
for i in colist17:
	if i:
		counter17 += 1
##############################################################
file18 = open('wifi.py','r')
counter18 = 0
content18 = file18.read()
colist18 = content18.split('\n')
for i in colist18:
	if i:
		counter18 += 1
###############################################################
file19 = open('/home/divyanshu/.oof.py','r')
counter19 = 0
content19 = file19.read()
colist19 = content19.split('\n')
for i in colist19:
	if i:
		counter19 += 1
###############################################################
total = counter1+counter2+counter3+counter4+counter5+counter6+counter7+counter8+counter9+counter11+counter12+counter13+counter14+counter15+counter16+counter17+counter18+counter19
total1 = total + 149
print(color.red+color.bold+'\nTotal number of lines in all the programs:\t'+color.end,total1)
