import sys
from collections import deque

moves = [(0,1),(1,0),(0,-1),(-1,0)]
def in_range(nx,ny):
    return 0<=nx<h and 0<=ny<w
def BFS():
    global cnt
    dq=deque()
    dq.append((0,0))
    visit = [[0] * (w + 2) for _ in range(h + 2)]
    visit[0][0]=1
    visit_docs = []  # 방문한 비밀문서 위치
    
    while dq:
        x,y = dq.popleft()
        visit[x][y]=1
        for dx,dy in moves:
            nx=x+dx
            ny=y+dy
            if nx<0 or nx>=h+2 or ny<0 or ny>=w+2 or board[nx][ny]=='*' or visit[nx][ny]==1:
                continue
            # 문 도달 
            if 'A' <= board[nx][ny] <= 'Z':      
                if board[nx][ny].lower() not in keys:   # 열 수 없음 
                    continue                
                else:
                    board[nx][ny]='.'                   
            # 열쇠면
            elif 'a' <= board[nx][ny] <= 'z':   
                keys.append(board[nx][ny])
                board[nx][ny]='.'
                visit = [[0] * (w + 2) for _ in range(h + 2)]
            # 첫 방문 비밀 문서 이면 
            elif board[nx][ny] == '$' and (nx,ny) not in visit_docs:
                cnt += 1
                board[nx][ny]='.'
                visit_docs.append((nx,ny))
            # 그냥 통로거나, 열쇠거나, 열수있는 문이면 
            dq.append((nx,ny))
            visit[nx][ny]=1

T=int(input())
for _ in range(T):
    h,w=map(int, input().split())
    board = [['.'] + list(map(str, input().rstrip())) + ['.'] for _ in range(h)]
    board = [['.'] * (w + 2)] + board + [['.'] * (w + 2)]
    keys = list(map(str, input().rstrip()))

    cnt=0    
    
    BFS()                
    print(cnt)