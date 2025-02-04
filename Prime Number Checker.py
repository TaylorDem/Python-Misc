# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 20:40:08 2025

Checks if the number is prime.

@author: demar
"""

import math

print("Is it prime?")
number = eval(input("Enter Number: "))
answer = True

if number & 1 == 0 and number != 2:     #"bitwise and" is the symbol '&'. 
    answer = False      #any number is even if the bit on the end is a 0.
    print("All even numbers besides 2 are not prime.", end="\n")
                        
if answer:
    for n in range(3, math.ceil(number/2), 2):
        print("checking factor: ", n, end="\n")
        #print(n, end="\n")
        if number % n == 0:
            answer = False
            break

if answer: print("Answer: Yes", end="\n")
if not answer: print("Answer: No", end="\n")