import sys
input=sys.stdin.readline
from collections import deque

dx=[-1,0,1,0]
dy=[0, 1, 0, -1]

r,c=map(int , input().split())
a=[list(input().rstrip()) for _ in range(r)]
boolean=False
for i in range(r):
    for j in range(c):
        if a[i][j]=='W':
            for k in range(4):
                xx=i+dx[k]
                yy=j+dy[k]
                if 0<=xx<r and 0<=yy<c:
                    if a[xx][yy]=='S':
                        boolean=True
                        break
if boolean:
    print(0)
else:
    print(1)
    for i in range(r):
        for j in range(c):
            if a[i][j]=='.':
                a[i][j]="D"
        
    for k in a:
        print(''.join(k))         

