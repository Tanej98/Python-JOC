# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

def choose():
    words=['computer','science','google','microsoft','linux','system','rainbow','yellow','animal','address','affect','analysis','article','appear','authority','benefit','blood','blue']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,"your score is",p1)
    print(p2n,"your score is",p2)
    print("Thanks for playing. Have a nice day.....")

def play():
    print("Let's stard the Jumbled Word game.....")
    p1name=input("player 1 , enter your name : ")
    p2name=input("player 2 , enter your name : ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print("jumbled word is",qn)
        if turn%2==0:
            print(p1name,'your turn.')
            ans=input("what's in my mind : ")
            if ans==picked_word:
                pp1 +=1
            else:
                print("better luck next time. I thought",picked_word )
            c=int(input("press 1 to continue and 0 to quit : "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        else:
            print(p2name,'your turn.')
            ans=input("what's in my mind : ")
            if ans==picked_word:
                pp2 +=1
            else:
                print("better luck next time. I thought",picked_word )
            c=int(input("press 1 to continue and 0 to quit : "))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
        turn += 1
play()