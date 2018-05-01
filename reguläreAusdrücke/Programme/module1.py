#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      localadmin
#
# Created:     24.04.2018
# Copyright:   (c) localadmin 2018
# Licence:     <your licence>
#------------------------------------------------------------------------------
import re

d = {"München": "MUC", "Budapest": "BUD", "Helsinki": "HEL"}
for key in d:
    value = d[key]
    print(key)
    print(value)
    print(value)
    print(key)

for key, value in d.items():
    print(key + ": " + value)


filepath = 'protokoll.txt'
with open(filepath) as fp:
   line = fp.readline()
   laenge = len(line)
   cnt = 1
   #mo = re.findall("[force]MAKE_EXEC_DATE_RAW.*", line)
   #print(mo)

   while line:
       line = fp.readline()
       mo = re.findall("NO WARRANTY.*", line)
       if mo :
            #print("Line {}: {} {}".format(cnt, laenge, line.strip()))
            print (mo)
            print("Line {}: {} {}".format(cnt, laenge, mo, line.strip()))
            laenge = len(line) # = 10
            #print(laenge)                              make
            line = fp.readline()
            mo = re.findall("NO WARRANTY", line)
            #print(mo)
            #print("Matching {}: {}".format(cnt, mo, line.strip()))

       cnt += 1
