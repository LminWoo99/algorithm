dx=[-1,0,1,0]
dy=[0,1,0,-1]
from collections import deque
def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0])
    
    visit=[[0]*m for _ in range(n)]
    def BFS(x,y):
        visit[x][y]=1
        dq=deque()
        cnt=0
        dq.append((x,y))
        while dq:
            x,y=dq.popleft()
            cnt+=int(maps[x][y])
            for i in range(4):
                xx , yy = x+dx[i], y+dy[i]
                if 0<=xx<n and 0<=yy<m:
                    if visit[xx][yy]==0 and maps[xx][yy]!='X':
                        visit[xx][yy]=1
                        dq.append((xx,yy))
        return cnt
    flag=False
    for i in range(n):
        for j in range(m):
            if maps[i][j]!='X' and visit[i][j]==0:
                cnt=BFS(i,j)
                answer.append(cnt)
                flag=True
    if not flag:
        answer.append(-1)
    answer.sort()
    return answer
print(solution(["XXX","XXX","XXX"]))