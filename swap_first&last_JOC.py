# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 07:55:09 2018

@author: KATA_TANEJ_KUMAR
"""
def swap(n):
    count=0
    original=n
    while original>0:
        original=int(original/10)
        count+=1
    last=n%10
    first=int(n/(10**(count-1)))
    n=int(n/10)
    n=n%(10**(count-2))
    return last*(10**(count-1))+n*10+first
n=int(input('enter the number : '))
print(swap(n))