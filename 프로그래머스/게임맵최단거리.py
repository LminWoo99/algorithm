from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def solution(maps):
    answer = 0
    n=len(maps)
    m=len(maps[0])
    visit=[[0]*m for _ in range(n)]
    def BFS(x,y):
        dq=deque()
        dq.append((x,y,1))
        visit[x][y]=1
        while dq:
            x,y,cnt=dq.popleft()
            
            if x==n-1 and y==m-1:
                return cnt
            for i in range(4):
                xx,yy=x+dx[i], y+dy[i]
                if 0<=xx<n and 0<=yy<m and maps[xx][yy] and not visit[xx][yy]:
                    visit[xx][yy]=1
                    dq.append((xx,yy, cnt+1))
    answer=BFS(0,0)    
    if not answer:
        answer=-1
    return answer