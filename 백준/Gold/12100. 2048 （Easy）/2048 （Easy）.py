import sys
from copy import deepcopy
n=int(input())
## 합쳐지는건 한번
board=[list(map(int, input().split())) for _ in range(n)]
def DFS(L,board):
    if L==5:
        return max(map(max, board))
    return max(DFS(L+1, up(deepcopy(board))), DFS(L+1, down(deepcopy(board))),DFS(L+1, left(deepcopy(board))),DFS(L+1, right(deepcopy(board))))
    
def up(board):
    for j in range(n):
        pointer=0
        for i in range(1,n):
            if board[i][j]:
                tmp=board[i][j]
                board[i][j]=0
                if board[pointer][j]==0:
                    board[pointer][j]=tmp
                elif board[pointer][j]==tmp:
                    board[pointer][j] *=2
                    pointer +=1
                else:
                    pointer +=1
                    board[pointer][j]=tmp
    return board
def down(board):
    for j in range(n):
        pointer=n-1
        for i in range(n-2, -1, -1):
            if board[i][j]:
                tmp=board[i][j]
                board[i][j]=0
                if board[pointer][j]==0:
                    board[pointer][j]=tmp
                elif board[pointer][j]==tmp:
                    board[pointer][j]*=2
                    pointer-=1
                else:
                    pointer-=1
                    board[pointer][j]=tmp
    return board
def right(board) :
    for i in range(n):
        pointer=n-1
        for j in range(n-2,-1,-1):
            if board[i][j]:
                tmp=board[i][j]
                board[i][j]=0
                if board[i][pointer]==0:
                    board[i][pointer]=tmp
                elif board[i][pointer]==tmp:
                    board[i][pointer]*=2
                    pointer-=1
                else:
                    pointer-=1
                    board[i][pointer]=tmp
    return board
def left(board):
    for i in range(n):
        pointer=0
        for j in range(1, n):
            if board[i][j]:
                tmp=board[i][j]
                board[i][j]=0
                if board[i][pointer]==0:
                    board[i][pointer]=tmp
                elif board[i][pointer]==tmp:
                    board[i][pointer]*=2
                    pointer+=1
                else:
                    pointer+=1
                    board[i][pointer]=tmp
    return board
print(DFS(0,board))