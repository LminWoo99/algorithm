import sys
input=sys.stdin.readline
from collections import deque
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def delete(a):
    for x,y in a:
        puyo[x][y]='.'
def down(): 
    for i in range(10, -1, -1):
        for j in range(6):
            if puyo[i][j]!='.' and puyo[i+1][j]=='.':
                cnt=i+1
                while True:
                    if puyo[cnt][j]=='.':
                        cnt+=1
                    else:
                        puyo[cnt-1][j]=puyo[i][j]
                        puyo[i][j]='.'
                        break           
                    if cnt==12:
                        puyo[cnt-1][j]=puyo[i][j]
                        puyo[i][j]='.'
                        break
def BFS(x,y):
    dq=deque()
    dq.append((x,y,1))
    cand.append([x,y])
    visit[x][y]=1
    while dq:
        x,y,cnt=dq.popleft()
        for i in range(4):
            xx,yy=x+dx[i], y+dy[i]
            if 0<=xx<12 and 0<=yy<6 and not visit[xx][yy] and puyo[x][y]==puyo[xx][yy]:
                visit[xx][yy]=1
                cand.append([xx,yy])
                dq.append((xx,yy, cnt+1))
res=0
puyo=[list(input().rstrip()) for _ in range(12)]
while True:
    visit=[[0]*6 for _ in range(12)]
    flag=False
    for i in range(12):
        for j in range(6):
            if puyo[i][j]!='.' and not visit[i][j]:
                cand=[]
                BFS(i,j)
                if len(cand)>=4:
                    flag=True
                    delete(cand)
    if flag:
        res+=1
        down()
    else:
        break
print(res)