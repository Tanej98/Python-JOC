# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 07:49:09 2018

@author: KATA_TANEJ_KUMAR
"""

import random
print('choose a door and win a BMW',
      'door_0 door_1 door_2 ')
swap=0
dont_swap=0
y=0
while y<20:
    doors=[0]*3
    goatdoors=[]
    x=random.randint(0,2)
    doors[x]='BMW'
    for i in range(3):
        if i==x:
             continue
        else:
            goatdoors.append(i)
    choice=int(input('enter your choice : '))
    door_open=random.choice(goatdoors)
    while door_open==choice:
        door_open=random.choice(goatdoors)
    print('door',door_open,'do not contain BMW')
    ch=input('do u want to change door y/n ?')
    if ch=='y':
        if choice==x:
            print('you lost')
        else:
            print('you won BMW')
            swap+=1
    else:
       if choice==x:
            print('you won BMW')
            dont_swap+=1
       else:
           print('you lost')
    y+=1
print(swap)
print(dont_swap)
    
    