dx=[-1,0,1,0]
dy=[0,1,0,-1]
from collections import deque
def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                startX, startY= i,j
            elif maps[i][j]=='L':
                leverX, leverY = i, j
            elif maps[i][j]=='E':
                endX, endY= i,j
    def BFS(x,y, resX, resY):
        dq=deque()
        dq.append((x,y,0))
        visit=[[0]*m for _ in range(n)]
        visit[x][y]=1
        while dq:
            x,y,cnt=dq.popleft()
            if x==resX and y==resY:
                return cnt
            for i in range(4):
                xx, yy = x+dx[i], y+dy[i]
                if 0<=xx<n and 0<=yy<m and maps[xx][yy]!='X' and visit[xx][yy]==0:
                    visit[xx][yy]=1
                    dq.append((xx,yy, cnt+1))
        return -1
    cand=BFS(startX, startY, leverX, leverY)
    if cand!=-1:
        cand_end=BFS(leverX, leverY, endX, endY)
        if cand_end==-1:
            answer=-1
        else:
            answer=cand+cand_end
    else:
        answer=-1

    return answer
print(solution(["SOOOL", "XXXXX", "OOOOO", "OXXXX", "OOOOE"]))