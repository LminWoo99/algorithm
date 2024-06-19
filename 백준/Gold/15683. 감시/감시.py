import sys
input=sys.stdin.readline
import copy
def DFS(L, cctv):
    global res
    if L==len(target):
        count=0
        for i in range(n):
            count+=cctv[i].count(0)
        res=min(res, count)
        return
    temp=copy.deepcopy(cctv)
    num,x,y=target[L]
    for i in mode[num]:
        fill(temp, i, x,y)
        DFS(L+1, temp)
        temp=copy.deepcopy(cctv)
def fill(cctv, mode, x, y):
    for i in mode:
        nx=x
        ny=y
        while True:
            nx+=dx[i]
            ny+=dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                break
            if cctv[nx][ny]==6:
                break
            elif cctv[nx][ny]==0:
                cctv[nx][ny]= -1

n,m = map(int, input().split())
cctv=[list(map(int, input().split())) for _ in range(n)]
dx=[0,1,0 ,-1]
dy=[1,0, -1, 0]
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],]
target=[]
for i in range(n):
    for j in range(m):
        if cctv[i][j] in [1,2,3,4,5]:
            target.append((cctv[i][j], i, j))
res=int(1e9)
DFS(0, cctv)
print(res)