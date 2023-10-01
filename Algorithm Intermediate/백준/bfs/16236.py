import sys
input=sys.stdin.readline()
from collections import deque
def BFS(x,y):
    while dq:
        dq.popleft()
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

dq=deque()
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    for j in range(n):
        if 1<=a[i][j]<=6:
            dq.append((i,j,a[i][j]))
        elif a[i][j]==9:
            x,y=i,j
            
BFS(i,j)