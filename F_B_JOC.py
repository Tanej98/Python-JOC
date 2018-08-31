# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 11:53:46 2018

@author: KATA_TANEJ_KUMAR
"""
i=int(input("enter the max number : "))
for n in range(1,i):
    if n%3==0:
        if n%5==0:
            print("FizzBizz")
        else:
            print("Fizz")
    elif n%5==0:
        print("Bizz")
    else:
        print(n)