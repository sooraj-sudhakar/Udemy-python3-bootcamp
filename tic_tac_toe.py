#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 09:11:05 2019

@author: Sooraj
"""

from IPython.display import clear_output

board=["","","","","","","","","","",""]

def display_board(board):
    clear_output()
    print(("\n| {0} | {1} | {2} |").format(board[7],board[8],board[9]))
    print("----------")
    print(("| {0} | {1} | {2} |").format(board[4],board[5],board[6]))
    print("----------")
    print(("| {0} | {1} | {2} |").format(board[1],board[2],board[3]))

def player_input():
    while True:
        try:
            player_in=int(input("Enter a number between 1-9 : "))
            while (player_in>0 and player_in<10):
                return player_in
            else:
                print("Only numbers between 1-9 allowded !")
        except:
            print("Only integers allowded !")
            
def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board, mark):
    indexs=[i for i, x in enumerate(board) if x==mark]
    diagonal_match=[[1,5,9],[3,5,7]]
    vertical_match=[[1,4,7],[2,5,8],[3,6,9]]
    horizontal_match=[[1,2,3],[4,5,6],[7,8,9]]

    def matcher(List,indexs):
        out=[]
        for i in range(0,len(List)):
            if (set(List[i]).issubset(set(indexs))==True):
                out.append('Won')
                #return ('{} won '.format(mark))
            else:
                out.append('Not won')
        return out
    return[matcher(diagonal_match,indexs),matcher(vertical_match,indexs),matcher(horizontal_match,indexs)]
    
def choose_first():
    while True:
        yield 'Player1'
        yield 'Player2'

def space_check(board, position):
    if (0<position<11):
        try:
            if board[position]!="":
                return False
            else:
                return True
        except:
            return True
    else:
        print('Out of range')

def full_board_check(board):
    if (board.count("")==0):
        return True
    else:
        return False

def player_choice(board):
    next_input=int(input('Enter the next position number 1-9 : '))
    if (0<next_input<10):
        if space_check(board,next_input)==True:
            return next_input

def replay():
    again=input('Do you want to play again ? y/n')
    if again=='y':
        return True
    else:
        return False

print("\nWelcome to Tic tac toe !")
test_board=["","1","2","3","4","5","6","7","8","9"]
display_board(test_board)
a=choose_first()
selection=next(a)
player1_symb=input("\n{} select the symbol (X or O) :  ".format(selection))
player1_symb=(player1_symb.upper()).strip()
if ((player1_symb=='X') or (player1_symb=='O')):
    if (player1_symb=='X'):
        player2_symb='O'
    else:
        player2_symb='X'
else:
    print("\nWrong option")
    
print("\nPlayer1 selected {}".format(player1_symb))
print("Player2 selected {}".format(player2_symb))   

while True:  
    # player 1 turn
    print("\nPlayer 1 turn")
    if (full_board_check(board)==False):
        p1_in = player_input()
        if(space_check(board,p1_in)==True):
            board=place_marker(board, player1_symb, p1_in)
            check1=['Won' in x for x in win_check(board,'X')]
            check2=['Won' in x for x in win_check(board,'O')]
            val1=True in check1
            val2=True in check2
            if((val1 is True) or (val2 is True)):
                print('\n'+'\033[1m'+"Player 1 won!!")
                display_board(board)
                break
            else:
                display_board(board)

        else:
            print("\nSlot already used !")
            pass
    else:
        print("\n Game over. Try again !")
        break

    # player 2 turn
    print("\nPlayer 2 turn")
    if (full_board_check(board)==False):
        p2_in = player_input()
        if(space_check(board,p2_in)==True):
            board=place_marker(board, player2_symb, p2_in)
            check1=['Won' in x for x in win_check(board,'X')]
            check2=['Won' in x for x in win_check(board,'O')]
            val1=True in check1
            val2=True in check2
            if((val1 is True) or (val2 is True)): 
                print('\n'+'\033[1m'+"Player 2 won!!")
                display_board(board)
                break
            else:
                display_board(board)
        else:
            print("\nSlot already used !")
            pass
    else:
        print("\n Game over. Try again !")
        break
