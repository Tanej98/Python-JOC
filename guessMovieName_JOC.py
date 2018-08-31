# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 08:58:44 2018

@author: KATA_TANEJ_KUMAR
"""
import random

movies=['avatar','tarzan','avengers','titanic','orphan','jungle book','dangal','sultan']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn

def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref=list(movie)
    n=len(movie)
    qn_list=list(qn)
    temp=[]
    for i in range(n):
        if (ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if qn_list[i]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new

def play():
    p1name=input('Player1 !enter the name: ')
    p2name=input('player2 !enter the name: ')
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1name,'your turn!')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input('your letter : ')
                if is_present(letter,picked_movie):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input('press 1 to guess movie name or 2 to unclock another letter :')
                    if d==str(1):
                        ans=input('enter the movie name :')
                        if ans==picked_movie:
                            pp1+=1
                            print('correct')
                            not_said=False
                            print(p1name,'your score is',pp1)
                        else:
                            print('wrong answer')
                else:
                    print(letter,'not found. try again :')
            c=int(input('press 1 to continue gaame or 0 to quit :'))
            if c==0:
                willing=False
                print(p1name,'your score is',pp1)
                print(p2name,'your score is',pp2)
                print('thanks for playing .Have a nice day')
        else:
            print(p2name,'your turn!')
            picked_movie=random.choice(movies)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input('your letter : ')
                if is_present(letter,picked_movie):
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input('press 1 to guess movie name or 2 to unclock another letter :')
                    if d==str(1):
                        ans=input('enter the movie name :')
                        if ans==picked_movie:
                            pp2+=1
                            print('correct')
                            not_said=False
                            print(p2name,'your score is',pp2)
                        else:
                            print('wrong answer')
                else:
                    print(letter,'not found. try again :')
            c=int(input('press 1 to continue gaame or 0 to quit :'))
            if c==0:
                willing=False
                print(p1name,'your score is',pp1)
                print(p2name,'your score is',pp2)
                print('thanks for playing .Have a nice day')
        turn+=1
play()