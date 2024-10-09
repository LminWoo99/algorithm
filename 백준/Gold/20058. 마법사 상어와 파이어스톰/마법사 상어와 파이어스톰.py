import sys, copy
from collections import deque
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,1,0,-1]
def rotate(level):
    for start in range(0, len(board), level):
        for end in range(0, len(board), level):
            tmp=[row[end:end+level] for row in board[start:start+level]]
            rotate_tmp=list(zip(*tmp[::-1]))
            for i in range(start , start+level):
                for j in range(end, end+level):
                    board[i][j]=rotate_tmp[i-start][j-end]
def check():
    tmp=len(board)
    temp=copy.deepcopy(board)
    for i in range(tmp):
        for j in range(tmp):
            if temp[i][j]:
                cnt=0
                for k in range(4):
                    ii,jj=dx[k]+i, dy[k]+j
                    ## 주변이 하나라도 얼음이 있으면 탈출
                    if 0<=ii<tmp and 0<=jj<tmp and temp[ii][jj]:
                        cnt+=1
                if cnt<3:
                    board[i][j]-=1
def BFS():
    dq=deque()
    visit=[[0]*len(board) for _ in range(len(board))]
    max_res=0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]:
                dq.append((i,j))
                visit[i][j]=1
                cnt=0
                while dq:
                    x,y=dq.popleft()
                    cnt+=1
                    for k in range(4):
                        ii,jj=dx[k]+x, dy[k]+y
                        if 0<=ii<len(board) and 0<=jj<len(board) and board[ii][jj] and not visit[ii][jj]:
                            dq.append((ii,jj))
                            visit[ii][jj]=1
                max_res=max(max_res, cnt)
    return max_res
                        
        
n,q=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(2**n)]

## 마법사 시전한 단계
magic_list=list(map(int, input().split()))
for i in range(q):
    cur_level=magic_list[i] # 현재 마법 단계
    cur_magic_list= [row[:2**cur_level] for row in board[:2**cur_level]]
    rotate(2**cur_level)
    check()

print(sum(map(sum, board)))
print(BFS())