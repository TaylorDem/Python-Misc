# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 23:58:48 2024

@author: demar
"""

with open('Exercise 2/data_values.txt', 'r') as f:
    lines = f.readlines()
    print(f'{"Name":<8s} | {"Measure 1":>7s} | {"Measure 2":>7s} | {"Measure 3":>7s}')
    print("-"*44)
    for line in lines:
        name, m1, m2, m3 = line.split()
        print(f'{name:<8s} | {int(m1):>+9d} | {float(m2):>-9.3f} | {float(m3):>-7g}')