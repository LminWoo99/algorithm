from collections import deque
import copy
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def solution(maze):
    answer = int(1e9)
    red_start, red_end=(0,0), (0,0)
    blue_start, blue_end=(0,0),(0,0)
    n,m= len(maze),len(maze[0])
    for i in range(n):
        for j in range(m):
            if maze[i][j]==1:
                red_start= (i,j)
            elif maze[i][j]==2:
                blue_start= (i,j)
            elif maze[i][j]==3:
                red_end=(i,j)
            elif maze[i][j]==4:
                blue_end=(i,j)
    
#     0이 red 1이 blue
    def BFS(red_start, blue_start, answer):
        visit=[[[0]*2 for _ in range(m)] for _ in range(n)]
        dq=deque()
        visit[red_start[0]][red_start[1]][0]=1
        visit[blue_start[0]][blue_start[1]][1]=1
        dq.append((red_start[0],red_start[1], blue_start[0], blue_start[1], 0, visit))
        while dq:
            x,y,x1,y1, cnt, visit=dq.popleft()
            if (x==red_end[0] and y==red_end[1]) and (x1==blue_end[0] and y1==blue_end[1]):
                answer=min(answer, cnt)
                continue
            if (x==red_end[0] and y==red_end[1]):
                for j in range(4):
                    xx1,yy1=x1+dx[j],y1+dy[j]
                    if 0<=xx1<n and 0<=yy1<m and visit[xx1][yy1][1]==0 and maze[xx1][yy1]!=5 and not (x==xx1 and y==yy1):
                            new_visit=copy.deepcopy(visit)
                            new_visit[xx1][yy1][1]=1
                            dq.append((x,y,xx1,yy1, cnt+1, new_visit))
            elif (x1==blue_end[0] and y1==blue_end[1]):
                for i in range(4):
                    xx,yy=x+dx[i],y+dy[i]
                    if 0<=xx<n and 0<=yy<m and visit[xx][yy][0]==0 and maze[xx][yy]!=5 and not (xx==x1 and yy==y1):
                        new_visit=copy.deepcopy(visit)
                        new_visit[xx][yy][0]=1
                        dq.append((xx,yy,x1,y1, cnt+1, new_visit))
            else:
                for i in range(4):
                    xx,yy=x+dx[i],y+dy[i]
                    if 0<=xx<n and 0<=yy<m and visit[xx][yy][0]==0 and maze[xx][yy]!=5:
                        for j in range(4):
                            xx1,yy1=x1+dx[j],y1+dy[j]
                            if 0<=xx1<n and 0<=yy1<m and visit[xx1][yy1][1]==0 and maze[xx1][yy1]!=5 and not ((xx==xx1) and (yy==yy1)):
                                if (xx==x1) and (yy==y1) and (xx1==x) and (yy1==y):continue
                                new_visit=copy.deepcopy(visit)
                                new_visit[xx][yy][0]=1
                                new_visit[xx1][yy1][1]=1
                                dq.append((xx,yy,xx1,yy1, cnt+1,new_visit))
        return answer
    answer=BFS(red_start, blue_start, answer)    
    if answer==int(1e9):
        return 0
    return answer
print(solution([[4, 3, 0, 0], [5, 5, 5, 0], [1, 0, 0, 0], [2, 0, 0, 0]]))
