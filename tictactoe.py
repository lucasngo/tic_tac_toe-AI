"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    count_x=0
    count_o=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                count_x+=1
            elif board[i][j]=='O':
                count_o+=1
    if count_x==count_o:
        return 'X'
    elif count_x>count_o:
        return 'O'
    else:
        print('player error')


def actions(board):
    poss_act=set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==None:
                poss_act.add((i,j))
    return list(poss_act)

def result(board, action):
    from copy import copy,deepcopy
    x=board
    new=deepcopy(x)
    new[action[0]][action[1]]=player(board)
    return new

def winner(board):
    winner_state=[[(0,0),(1,1),(2,2)],
                    [(0,0),(0,1),(0,2)],
                    [(1,0),(1,1),(1,2)],
                    [(2,0),(2,1),(2,2)],
                    [(0,0),(1,0),(2,0)],
                    [(0,1),(1,1),(2,1)],
                    [(0,2),(1,2),(2,2)],
                    [(0,2),(1,1),(2,0)]]
    X_pos=[]
    Y_pos=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='X':
                X_pos.append((i,j))
            elif board[i][j]=='O':
                Y_pos.append((i,j))
            else:
                pass
    
    for i in range(len(winner_state)):
        count_x=0
        count_y=0
        for j in range(len(winner_state[0])):
            if winner_state[i][j] in X_pos:
                count_x+=1
            elif winner_state[i][j] in Y_pos:
                count_y+=1
            
            if count_x==3:
                return 'X'
            elif count_y==3:
                return 'O'
    return None


def terminal(board):
    
    if winner(board) != None:
        return True
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==None:
                return False

    return True


def utility(board):
    win=winner(board)
    
    if win=='X':
        point=1
        return point
    elif win=='O':
        point=-1
        return point
    else:
        return 0




def maxvalue(board):
    if terminal(board):
        return utility(board)
    v=-999
    for action in actions(board):
        v= max(v,minvalue(result(board,action)))
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)
    v=999
    for action in actions(board):
        v= min(v,maxvalue(result(board,action)))
    return v


def minimax(board):
    dict_ans={}
    action=actions(board)
    if player(board)=='X':
        for action in action:
            new=result(board,action)
            point=minvalue(new)
            dict_ans[action]=point
        
        sort_order = sorted(dict_ans.items(), key=lambda x: x[1],reverse=True)
        print(sort_order)
        return sort_order[0][0]
    elif player(board)=='O':
        for action in action:
            new=result(board,action)
            point=maxvalue(new)
            dict_ans[action]=point
        
        sort_order = sorted(dict_ans.items(), key=lambda x: x[1])
        print(sort_order)
        return sort_order[0][0]
