# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:46:54 2018

@author: KATA_TANEJ_KUMAR
"""
import random
import string
symbols=[]
card1=[0]*5
card2=[0]*5
symbols=list(string.ascii_letters)
pos1=random.randint(0,4)
pos2=random.randint(0,4)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if pos1==pos2:
    card1[pos1]=samesymbol
    card2[pos1]=samesymbol
else:
    card1[pos1]=samesymbol
    card2[pos2]=samesymbol
    card1[pos2]=random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1]=random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while i<5:
    if (i!=pos1 and i!=pos2):
        element1=random.choice(symbols)
        symbols.remove(element1)
        element2=random.choice(symbols)
        symbols.remove(element2)
        card1[i]=element1
        card2[i]=element2
    i+=1
print(card1)
print(card2)
ch=input('enter the similar symbol : ')
if ch==samesymbol:
    print('rigth')
else:
    print('wrong')