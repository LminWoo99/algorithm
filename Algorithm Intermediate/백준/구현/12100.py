import sys
input=sys.stdin.readline
from copy import deepcopy
n=int(input())
block=[list(map(int, input().split())) for _ in range(n)]
    
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
                    board[pointer][j] = tmp
                elif board[pointer][j] == tmp :
                    board[pointer][j] *= 2
                    pointer-=1
                else:
                    pointer-=1
                    board[pointer][j]=tmp
    return board               
 # LEFT
def left(board):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    board[i][pointer]= tmp
    return board

# RIGHT
def right(board):
    for i in range(n):
        pointer = n - 1
        for j in range(n - 2, -1, -1):
            if board[i][j]:
                tmp = board[i][j]
                board[i][j] = 0
                if board[i][pointer] == 0:
                    board[i][pointer] = tmp
                elif board[i][pointer]  == tmp:
                    board[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    board[i][pointer] = tmp
    return board
res=0
def DFS(board, L):
    if L==5:
        return max(map(max, board))

    return max(DFS(up(deepcopy(board)), L+1), DFS(down(deepcopy(board)), L+1), DFS(left(deepcopy(board)), L+1), DFS(down(deepcopy(board)), L+1))

res=DFS(block, 0)
print(res)
