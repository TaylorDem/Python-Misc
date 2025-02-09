# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:46:32 2024

@author: demar
"""

import re

with open('Exercise 4/data.txt', 'r') as f:
    lett_count = dict([('x', 0),('y', 0),('z', 0)])
    sum_float = 0.0
    sum_int = 0
    lines = f.readlines()
    expression = re.compile(r"""
                            ^(-?(?:(?:[1-9]\d*)|[0])\.\d+)\s+   # float
                            ((?:\+|-)?(?:(?:[1-9]\d*)|[0]))\s+  # integer
                            ((?:[x-z]|[X-Z]){3})$               # character
                            """, re.VERBOSE)
    for n in lines:
        m = expression.match(n)
        if m :
            #print(m.groups())
            raw_letts = m.group(3).lower()
            for l in raw_letts:
                if l == 'x':
                    lett_count['x'] += 1
                if l == 'y':
                    lett_count['y'] += 1
                if l == 'z':
                    lett_count['z'] += 1
            sum_float += float(m.group(1))
            sum_int += int(m.group(2))
        else:
            print("No match with " + n)
            
    print(f'Sum of floats: {sum_float:.3f}' + " Sum of Integers: " + str(sum_int))
    print(lett_count)
    
        