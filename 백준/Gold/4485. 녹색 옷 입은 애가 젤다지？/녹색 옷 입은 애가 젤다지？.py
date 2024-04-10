import sys
import heapq
input=sys.stdin.readline
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def soultion(x,y, L):
    visit[x][y]=L
    hq=[]
    heapq.heappush(hq, (L, x,y))
    while hq:
        L,x,y=heapq.heappop(hq)
        if L>visit[x][y]:
            continue
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<n and visit[xx][yy]>board[xx][yy]+L:
                visit[xx][yy]=L+board[xx][yy]
                heapq.heappush(hq, (L+board[xx][yy], xx,yy))
    return
j=1        
while True: 
    n=int(input().rstrip())
    if n==0:
        break
    board=[list(map(int, input().split())) for _ in range(n)]
    visit=[[int(1e9)]*n for _ in range(n)]
    soultion(0,0,board[0][0])
    print("Problem {}: {}".format(j,visit[n-1][n-1]))
    j+=1