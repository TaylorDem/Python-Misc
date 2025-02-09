# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 21:11:47 2024

@author: demar
"""
import numpy as np

A = np.matrix( [[1,2,3],[11,12,13],[21,22,23]])
b = np.matrix( [[1],[2],[3]] )


#dot product is row(A) x column(b).
#1x1+2x2+3x3
#1x11+2x12+3x13
#1x21+2x22+3x23


print(A*b)