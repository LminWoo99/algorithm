import sys
from copy import deepcopy
input=sys.stdin.readline

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

def DFS(board, cnt):
    if cnt==5:
        return max(map(max, board))
    # 상, 하, 좌, 우로 움직여 리턴한 값들 중 가장 큰 값 반환
    # board를 꼭 deepcopy하여 함수를 거친 board값이 다음 함수에 들어가지 못하도록 해주어야 한다.
    return max(DFS(up(deepcopy(board)), cnt + 1), DFS(down(deepcopy(board)), cnt + 1), DFS(left(deepcopy(board)), cnt + 1), DFS(right(deepcopy(board)), cnt + 1))
    
    
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
print(DFS(a,0))