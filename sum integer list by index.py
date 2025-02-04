# -*- coding: utf-8 -*-
"""
Produce Python code that prompts for and inputs 2 lists of numbers 
You needn’t verify that they are indeed lists of numbers 
It prints out a list where the element at any index i is the sum of the elements at index i of the 2 input lists 
If the input lists are of different lengths, have the length of the output list be the length of the shorter of the 2 
E.g., if the two input lists are [2, 4, 3] and [1, 7, 2, 5], then the resulting list will be [3, 11, 5]
Use a for loop 
Note that, where x and y are numbers, min(x,y) is the smaller of those 2 numbers

"""


x = eval(input("Enter first list: "))
y = eval(input("Enter second list: "))
z = []
for i in range(0,min(len(x),len(y))):
    z.insert(i, x[i] + y[i] )

print("The minimum length sum'd lists is: ", z)
