# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 13:05:02 2018

@author: KATA_TANEJ_KUMAR
"""
import random
def evolve(x):
    ind=random.randint(0,len(x)-1)
    p=random.randint(1,2)
    if p==1:
        if x[ind]=='0' :
            x[ind]=='1'
        else:
            x[ind]=='0'
    
with open("dna_JOC.txt") as dna:
    x=dna.read()
    x=list(x)
for i in range(0,10000):
    evolve(x)
print(x)