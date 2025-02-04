# -*- coding: utf-8 -*-
"""
Write a Python script that implements the following functions 
Don’t have any functions input or output values 
All values used by a function should be passed to it as arguments 
The value computed by a function should be returned, not output by the function
Use the test code shown below and provided on Blackboard 
It satisfies these constraints and outputs the results of all function applications for testing your implementations 
The test code assigns to lst a list of integers used as the running list for tests 
Beside being passed the running list of integers, any function could be passed any list of integers 

sum_threshold() is passed as its 1st argument an integer, call it , used as a threshold
This is followed by any number of other integer arguments 
It returns the sum of the arguments listed after , calculated from left to right until adding the next would exceed  
If the sum of all these arguments is  , then this sum is returned 
If only the  argument is provided, return 0 
Use the “arbitrary argument lists” technique, with * 
To use the list lst set at the beginning, unpack it (use a *) when you provide it as an argument 
You’ll be unpacking the list (with *) when you pass it in and packing the arguments back up (using again a *) in the argument list in the function definition 
The easy way to implement this involves a break 

pairs_factors() is passed the running list of integers, lst 
It returns a list of pairs (2-element tuples), one pair for each element of lst. In a given pair, 
the 1st element of a pair is the element of lst itself, call it x, and 
the 2nd element is the list of those elements of lst that are factors of x 
Note: neither 1 nor (for this problem, but not the previous) x counts as factors of x 
Implement this using a nested list comprehension 
Note: y is a  factor of x if and only if x % y == 0 (and y isn’t in {x, 1}) 
When performing this mod operation, guard against the case where y is 0, which amounts to division by 0 

"""

def sum_threshold(max, *list):
    if not list:
        return 0
    sum = 0
    for i in range(len(list)):
        if sum+list[i] >max:
            break
        else:
            sum += list[i]
    return sum

def pairs_factors(list):
    results = []
    for i in range(0,len(list)):
        factors = []
        for j in range(0,len(list)):
            if list[j] != 0 or list[j] != 1:
                if (list[i]%list[j]) == 0 and list[j] != list[i]:
                    factors.append(list[j])
        results.insert(i,(list[i],factors))
    return results
    

lst = [7, 2, 12, 9, 15, 4, 11, 5]
print('The sum of the elemenst, left to right, without exceeding the')
print('threshold 40 is ', sum_threshold(40, *lst))
print('The same but with a threshold of 70: ', sum_threshold(70, *lst))
print('With an empty list of numbers: ', sum_threshold(50))
print('pairs_factors(lst): ', pairs_factors(lst))
