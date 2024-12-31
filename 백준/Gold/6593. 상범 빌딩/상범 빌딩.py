dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]
import sys
input=sys.stdin.readline
from collections import deque
def find_start(list):
    n,m,k=len(list), len(list[0]) , len(list[0][0])
    for i in range(n):
        for j in range(m):
            for x in range(k):
                if list[i][j][x]=='S':
                    return i,j,x
def BFS(x,y,z):
    dq=deque()
    dq.append((x,y,z,0))
    visit[x][y][z]=1
    while dq:
        x,y,z,cnt=dq.popleft()
        if building[x][y][z]=='E':
            return cnt
        for i in range(6):
            xx,yy,zz=x+dx[i], y+dy[i], z+dz[i]
            if 0<=xx<l and 0<=yy<r and 0<=zz<c and not visit[xx][yy][zz] and building[xx][yy][zz]!='#':
                visit[xx][yy][zz]=1
                dq.append((xx,yy,zz,cnt+1))
    return -1
while True:
    l,r,c=map(int, input().split())
    if l==0 and r==0 and c==0:
        break
    building=[[[0]*c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        tmp=[list(input().rstrip()) for _ in range(r+1)]
        tmp.pop()
        for j in range(r):
            for k in range(c):
                building[i][j][k]=tmp[j][k]
    x,y,z=find_start(building)
    visit=[[[0]*c for _ in range(r)] for _ in range(l)]
    res=BFS(x,y,z)
    if res<0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." %res)