# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:04:41 2018

@author: KATA_TANEJ_KUMAR
"""

def bubble(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
    return a
p=[1,6,5,4,3,2]
print(bubble(p))