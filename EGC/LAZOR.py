import os

#Strings to be removed
st = ['G0 Z' , 'G1 Z-0.500 F150.0' , 'G1 Z-1.000 F150.0' , 'G1 Z-1.500 F150.0' , 'G1 Z-2.000 F150.0' , 'G1 Z-2.500 F150.0' , 'G1 Z1.500 F228.6']
#Strings to be inserted
sg = ['M106 P0 S0 ;' , 'M106 P0 S55' , 'M106 P0 S105' , 'M106 P0 S155' , 'M106 P0 S205' , 'M106 P0 S255' , ';G1 Z1.500 F228.6']
#inputfilename
rf = ""
fi = str(input('Enter file name (without .nc extension) \n >'))
rundir = str(os.getcwd())
if '/' in rundir:
	o = '/'
elif '\\' in rundir:
	o = '\\'
rd = rundir.split(o)
rd.pop()
rd.append(fi)                  
for i in range(len(rd)):
    if i == (len(rd) - 1):
        rf = rf +rd[i]
    else:
        rf = rf + rd[i] + o
print(rf)
filename = str(rf)
#creates tmp file, and does first conversion
fin = open(filename + '.nc', 'rt')
ftmp = open('tmp.txt', 'wt')
for line in fin:
	ftmp.write(line.replace('G1 Z2.000', ';G1 Z2.00'))
fin.close()
ftmp.close()


for x in range(len(st)):                                #loops through conversion strings creating and deleting second tmp file through each loop
        ftmp = open('tmp.txt', 'rt')
        ftmpx = open('tmp' + str(x) + '.txt', 'wt')
        for line in ftmp:                               #loops through file replacing st[x] string with sg[x] string.
                ftmpx.write(line.replace(st[x], sg[x]))
        ftmp.close()
        ftmpx.close()
        os.remove("tmp.txt")
        os.rename('tmp' + str(x) + '.txt', 'tmp.txt')

# Check for existing file and ask to overwrite or cancel        
if os.path.isfile(filename + '.gcode'):
        ain = str(input('Gcode file already exists. Would you like to overwrite? \n Y/N? \n'))
        if ain == 'Y' or ain == 'y':
                os.remove(filename + '.gcode')
                os.rename('tmp.txt', filename + '.gcode')
                print('Overwritten')
        elif ain == 'N' or ain == 'n':
                print('Canceled')
        else:
                print('You\'re a towel')
else:
        os.rename('tmp.txt', filename + '.gcode')
        print('Done')











