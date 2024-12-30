import sys , copy
from collections import deque
input = sys.stdin.readline
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def check(list):
    fires=[]
    for i in range(len(list)):
        for j in range(len(list[0])):
            if list[i][j]=='@':
                x,y=i,j
            elif list[i][j]=='*':
                fires.append([i,j])
    return x,y,fires
def BFS(x,y,fires):
    dq=deque()
    tmp=copy.deepcopy(maps)
    visit=[[0]*len(tmp[0]) for _ in range(len(tmp))]
    visit[x][y]=1
    dq.append((x,y,0))
    fire_cnt=-1
    while dq:
        x,y,cnt=dq.popleft()
        # print(x,y,cnt)
        temp=[]
        if x==0 or y==0 or x==len(tmp)-1 or y==len(tmp[0])-1:
            return cnt+1
        if fire_cnt!=cnt:
            for fireX, fireY in fires:
                for i in range(4):
                    xx, yy=fireX+dx[i], fireY+dy[i]
                    if 0<=xx<len(tmp) and 0<=yy<len(tmp[0]) and tmp[xx][yy]!='#' and tmp[xx][yy]!='*':
                        tmp[xx][yy]='*'
                        temp.append([xx,yy])            
            fires=temp[:]
            fire_cnt+=1
        for i in range(4):
            xx,yy=x+dx[i], y+dy[i]
            if 0<=xx<len(tmp) and 0<=yy<len(tmp[0]) and (tmp[xx][yy]=='.') and not visit[xx][yy]:
                visit[xx][yy]=1
                dq.append((xx,yy,cnt+1))
    return 0
t=int(input())
for _ in range(t):
    w,h = map(int, input().split())
    maps=[list(input().rstrip()) for _ in range(h)]
    x,y,fires=check(maps)   
    res=BFS(x,y,fires)
    if not res:
        print("IMPOSSIBLE")
    else:
        print(res)