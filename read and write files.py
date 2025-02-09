# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 21:06:27 2024

@author: demar
"""

with open('Exercise 2/data.txt', 'r') as f, \
     open('Exercise 2/out_data_float.txt', 'w') as writeFf, \
     open('Exercise 2/out_data_int.txt', 'w') as writeFi:
    lines = f.readlines()
    for n in lines[:-1]:        #process lines without the end line
        name, f1, f2, i1, i2 = n.split()
        writeFf.write("%s %.2f\n" % (name, float(f1) + float(f2)))
        writeFi.write("%s %d\n" % (name, int(i1) + int(i2)))
    #write last line with no \n
    name, f1, f2, i1, i2 = lines[-1].split()
    writeFf.write("%s %.2f" % (name, float(f1) + float(f2)))
    writeFi.write("%s %d" % (name, int(i1) + int(i2)))
