# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 20:44:43 2024

@author: demar
"""

def split_dict(x, D):
    lessThan = dict([(key,value) for key, value in D.items() if value < x])
    greaterThan = dict([(key2,value2) for key2, value2 in D.items() if value2 > x])
    return (lessThan, greaterThan)      
    
    
d = dict([('a', 2), ('b', 10), ('c', 2), ('d', 9), ('e', 5)])
x = 3
print(split_dict(x, d))


def select_by_weight(t, D):
    print(f'{"Name":8s} | {"Weight":5s}')
    print('-'*17)
    for k, v in D.items():
        if v >= t:
            print(f'{k:8s} | {v:<8.2f}')
    print()
    
d = {'Mike':190.5, 'Mary':130.25, 'Al':220.3, 'Sue':155.75} 
select_by_weight(150, d)