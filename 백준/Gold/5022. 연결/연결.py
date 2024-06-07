import sys
input=sys.stdin.readline
from collections import deque

def BFS(A1, A2):
    dq=deque()
    dq.append((*A1, *A1,0))
    while dq:
        x1,y1,last_x,last_y,dist=dq.popleft()
        if visit[x1][y1]:
            continue
        visit[x1][y1]=last_x,last_y
        if [x1,y1] == A2:
            return dist
        for i in range(4):
            next_x1,next_y1=x1+dx[i], y1+dy[i]
            if 0<=next_x1<=n and 0<=next_y1<=m:
                dq.append((next_x1, next_y1,x1,y1, dist+1))
    return 1e6
def check(A1,A2,B1,B2):
    global visit
    visit=[[0]*(m+1) for _ in range(n+1)]
    for x,y in [B1,B2]:
        visit[x][y]=1
    dist=BFS(A1, A2)
    if dist==1e6:
        return 1e6
    x,y=A2
    new_visit=[[0]*(m+1) for _ in range(n+1)]
    while 1:
        if new_visit[x][y]:
            break
        new_visit[x][y]=1
        x,y=visit[x][y]
    visit=new_visit
    return dist+BFS(B1, B2)

n,m=map(int, input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]

A1=list(map(int, input().split()))
A2=list(map(int, input().split()))
B1=list(map(int, input().split()))
B2=list(map(int, input().split()))
result_A = check(A1, A2, B1, B2)  
result_B = check(B1, B2, A1, A2)  
min_result = min(result_A, result_B)

if min_result > 1e5:
    print("IMPOSSIBLE")
else:
    print(min_result)

