# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 08:22:13 2018

@author: KATA_TANEJ_KUMAR
"""
def reverse(x):
   a=0
   b=len(x)-1
   while(a<=b):
       y=x[a]
       x[a]=x[b]
       x[b]=y
       a+=1
       b-=1
list_1=[1,2,3]
reverse(list_1)
print(list_1)
