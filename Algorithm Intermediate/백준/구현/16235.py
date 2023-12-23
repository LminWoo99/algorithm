import sys
input=sys.stdin.readline
from collections import deque
def spring_summer():
    for i in range(n):
        for j in range(n):
            tree_len=len(tree[i][j])
            for k in range(tree_len):
                if ground[i][j]<tree[i][j][k]:
                    for _ in range(k , tree_len):
                        die[i][j].append(tree[i][j].pop())
                    break
                else:
                    ground[i][j]-=tree[i][j][k]
                    tree[i][j][k]+=1
    for i in range(n):
        for j in range(n):
            while die[i][j]:
                ground[i][j]+=die[i][j].pop() // 2 
def autumn_winter():
    for i in range(n):
        for j in range(n):
            for k in range(len(tree[i][j])):
                if tree[i][j][k]%5==0:
                    for l in range(8):
                        xx , yy= dx[l]+i, dy[l]+j
                        if 0<=xx<n and 0<=yy<n:
                            tree[xx][yy].appendleft(1)
            ground[i][j]+=a[i][j]
    
        
n,m,k=map(int, input().split())
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]
die=[[list() for _ in range(n)] for _ in range(n)]
ground=[[5]*n for _ in range(n)]
a=[list(map(int, input().split())) for _ in range(n)]
tree=[[deque() for _ in range(n)] for _ in range(n)]

for i in range(m):
    x,y,z=map(int, input().split())
    tree[x-1][y-1].append(z)

for _ in range(k):
    spring_summer()
    autumn_winter()
result=0
for i in range(n):
    for j in range(n):
        result+=len(tree[i][j])
print(result)
