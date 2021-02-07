import os
ch = 'Y'
while ch == 'Y':
	print('In which format you want information')
	print('1.\t Megabyte')
	print('2.\t Bytes')
	y = int(input('Enter your choice:\t'))
	if y == 1:
		os.system('df -m')
	if y == 2:
		os.system('df')
	ch = input('Do you wnat to continue seeing disk informations in different formats:\t')
