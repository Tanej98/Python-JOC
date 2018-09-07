# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 19:29:48 2018

@author: KATA_TANEJ_KUMAR
"""

import string
dict={}
data=""
file=open("output.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-2]
with open("input.txt") as f:
    while True:
        c=f.read(1)
        if not c:
            print("End Of The File")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        file.write(data)
file.close()