# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 14:01:59 2018

@author: KATA_TANEJ_KUMAR
"""

import math
n=int(input())
up=[]
down=[]
right=[]
left=[]
for i in range(n):
  a,b=input().split()
  b=int(b)
  if a=='UP':
    up.append(b)
  elif a=='DOWN':
    down.append(b)
  elif a=='RIGHT':
    right.append(b)
  else:
    left.append(b)
w=0
x=0
y=0
z=0
for i in up:
  w+=i
for i in down:
  x+=i
for i in right:
  y+=i
for i in left:
  z+=i
w=w-x
y=y-z
v=math.sqrt(w**2 +y**2)
v=round(v)
print(v)
  