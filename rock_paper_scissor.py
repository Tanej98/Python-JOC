# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 18:05:31 2018

@author: KATA_TANEJ_KUMAR
"""
def rock_paper_scissor(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if player_one[p1]==player_two[p2]:
        print("draw")
    elif (player_one[p1]=='paper' and player_two[p2]=='rock'):
        print('player one wins')
    elif (player_one[p1]=='paper' and player_two[p2]=='scissor'):
        print('player two wins')
    elif (player_one[p1]=='rock' and player_two[p2]=='paper'):
        print("player two wins")
    elif (player_one[p1]=='rock' and player_two[p2]=='scissor'):
        print('player one wins')
    elif (player_one[p1]=='scissor' and player_two[p2]=='rock'):
        print('player two wins')
    elif (player_one[p1]=='scissor' and player_two[p2]=='paper'):
        print('player one wins')
player_one={0:'rock',1:'paper',2:'scissor'}
player_two={0:'scisssor',1:'rock',2:'paper'}
while(1):
    num1=input('Player one! Enter your choice :')
    num2=input('Player Two! Enter your choice :')
    bit1=int(input('Player one! Enter the secret bit position'))
    bit2=int(input('Player two! Enter the secret bit position'))
    rock_paper_scissor(num1,num2,bit1,bit2)
    ch=input('do yo want to continue y/n ?')
    if ch=='n':
        break
