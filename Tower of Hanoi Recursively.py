# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:52:01 2025

Tower of Hanoi Problem.
Recursion.
@author: demar
"""

def TowerC(A, B, C, n):  #A is starting point, B is the middle point, C is end point, N is number of pieces to move.
    if n==1: 
        print(A, '->', C)
        return
    TowerC(A, C, B, n-1)
    print(A, '->', C)
    TowerC(B, A, C, n-1)

print("Moving A to C")
TowerC("A", "B", "C", 3)


def TowerB(A, B, C, n):  #A is starting point, B is the middle point, C is end point, N is number of pieces to move.
    if n==1: 
        print(A, '->', B)
        return
    TowerB(A, C, B, n-1)
    print(A, '->', B)
    TowerB(C, B, A, n-1)
    
print("Moving A to B")
TowerB("A", "B", "C", 3)
