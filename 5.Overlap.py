# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 19:50:04 2016

@author: Vinod
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlap = list()
for item in a:
    if item in b and item not in overlap:
        overlap.append(item)
       
print(overlap)

## Single line random
import random
a= [random.randrange(1,100) for i in range(10)]
b= [random.randrange(1,100) for i in range(10)]
print(a)
print(b)
common=[]
common=[(item1) for item1 in a for item2 in b if item1==item2]
print(common)