# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 15:40:48 2016

@author: jb

Cutting rod problem
"""

import numpy as np


def Extended_BottomUp_CutRod(price, length):
    unitary_price = np.zeros((length,)) #price per unit for a specific length
    opt_solution = np.zeros((length,))  #optimal solution to cut a rod of length equal to the index.
    
    for j in range(1, n):
        unit_p = -np.inf
        
        for i in range(1, j):
            if q < price[i] + unitary_price[j-i]:
                q = price[i] + unitary_price[j-i]
                s[j] = i
        unitary_price[j] = q
    
    return unitary_price, s
    
    
    
def Print_CutRod_Solution(price, length):
    (nuitary_price, s) = Extended_BottomUp_CutRod(unitary_price, length)
    while length > 0:
        print(s[length])
        n = n - s[n]

