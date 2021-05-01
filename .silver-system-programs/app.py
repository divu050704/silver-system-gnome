import os
file = open('/usr/.silver-system-programs/Name.txt')
counter1 = 0
content1 = file.read()
colist1 = content1.split('\n')
for i in colist1:
    if i:
        counter1 += 1
file1 = open('/usr/.silver-system-programs/Name.txt')
con1 = file1.readlines()
print('Choose name of application from below')
for i in range(counter1):
    print(i,':\t',str(con1[i][5:]))
n = int(input('Enter your choice:\t'))
file2 = open('/usr/.silver-system-programs/Exec.txt')
con2 = file2.readlines()
main = str(con2[n])
main1 = main[5:]
#os.system(main1)
print(main1)
if ( '%U' in main1 ):
    ind=(str(main1.index('%U')))
    ind1 = int(ind)
    print(ind1)
    main2=(main1[0:ind1])
    os.system(main2)
if ( '%u' in main1 ):
    ind = (str(main1.index('%u')))
    ind1 = int(ind)
    print(ind1)
    main2=(main1[0:ind1])
    os.system(main2)
if ( 'Exec' in main1 ):
    ind = (str(main.index('Exec')))
    ind1 = int(ind)
    main2 = main1[0:ind1]
    os.system(main2)
if ( 'TryExec' in main1 ):
    ind = (str(main.index('TryExec')))
    ind1 = int(ind)
    main2 = main1[0:ind1]
    os.system(main2)
mainj = main[0:7]
if ('TryExec' in mainj):
    d = main[8:]
    if 'Exec' in d:
        ind = (str(d.index('Exec')))
        ind1 = int(ind)
        main2 = d[0:ind1]
        print(main2)
else:
    os.system(main1)
