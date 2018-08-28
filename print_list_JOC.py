# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 21:58:14 2018

@author: KATA_TANEJ_KUMAR
"""

list_1=[1,2,3,4]
list1=[[]]
length=len(list_1)
for i in range(0,length):
    for j in range(i+1,length+1):
        list1.append(list_1[i:j])
print(list1)