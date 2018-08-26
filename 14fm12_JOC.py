# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 07:49:01 2018

@author: KATA_TANEJ_KUMAR
"""

list1=[12,24,36,48,60,72,84,96,108,120]
incre=1
for i in range(0,10):
    list1[i]=list1[i]+incre*2
    incre+=1
print(list1)