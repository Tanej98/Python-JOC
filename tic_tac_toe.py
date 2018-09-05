# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 08:07:43 2018

@author: KATA_TANEJ_KUMAR
"""

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'

def check_row(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False

def check_column(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count=count+1
        if count==3:
            print(symbol,'won')
            return True
    return False

def check_diagonal(symbol):
    if (board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol):
        print(symbol,'won')
        return True
    if (board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol):
        print(symbol,'won')
        return True
    return False

def won(symbol):
    return (check_row(symbol) or check_column(symbol) or check_diagonal(symbol))

def place(symbol):
    print(numpy.matrix(board))
    while 1:
        row=int(input('enter the row - 1, 2 ,3 :'))
        col=int(input('enter the column - 1, 2, 3 :'))
        if (row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-') :
            break
        else:
            print('invalid input.enter again')
    board[row-1][col-1]=symbol

def play():
    for turn in range(9):
        if turn%2==0:
            print('X turn')
            place(p1s)
            if won(p1s):
                break
        else:
            print('O turn')
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)) :
        print('draw')

play()