import sys
from collections import deque
import heapq
input=sys.stdin.readline
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def BFS(x,y):
  hq=[]
  visit=[[0]*n for _ in range(n)]
  heapq.heappush(hq, (0, x, y))
  visit[x][y]=1
  cand=[]
  tmp=int(1e9)
  while hq:
    cnt,x,y=heapq.heappop(hq)
    for i in range(m):
      if not res_cand[i]:
        if passenger_start[i][0]==x and passenger_start[i][1]==y and cnt<=tmp:
          cand.append((x,y, i))      
          tmp=cnt
          break
    if cnt>tmp:
      break
    for i in range(4):
      xx,yy=x+dx[i], y+dy[i]
      if 0<=xx<n and 0<=yy<n and not visit[xx][yy] and board[xx][yy]==0:
        visit[xx][yy]=1
        heapq.heappush(hq, (cnt+1, xx,yy))
  return cand, tmp
def BFS_DEST(x,y, target):
  dq=deque()
  visit=[[0]*n for _ in range(n)]
  dq.append((x,y, 0))
  visit[x][y]=1
  while dq:
    x,y,cnt=dq.popleft()
    if x==passenger_end[target][0] and y==passenger_end[target][1]:
      return cnt
    for i in range(4):
      xx,yy=x+dx[i], y+dy[i]
      if 0<=xx<n and 0<=yy<n and not visit[xx][yy] and board[xx][yy]==0:
        visit[xx][yy]=1
        dq.append((xx,yy, cnt+1))
  return 0
n,m,k=map(int, input().split()) #격자 크기, 손님 수, 연료양
board=[list(map(int, input().split())) for _ in range(n)]
taxy_x, taxy_y=map(int, input().split()) # 택시 초기 위치
taxy_x-=1
taxy_y-=1

passenger_start = [] # 손님들의 출발지를 저장할 리스트
passenger_end = [] # 손님들의 도착지를 저장할 리스트
for _ in range(m):
    sy, sx, ey, ex = map(int, input().split())
    passenger_start.append([sy - 1, sx - 1])
    passenger_end.append([ey - 1, ex - 1])
res_cand=[0]*m
res=0
flag=True
while res<m:
  cand,tmp=BFS(taxy_x, taxy_y)
  k-=tmp
  if k<=0:
    flag=False
    break
  cand.sort(key=lambda x:(x[0], x[1]))
  temp=BFS_DEST(cand[0][0], cand[0][1], cand[0][2])
  if temp==0 or k-temp<0:
    flag=False
    break
  k-=temp
  res_cand[cand[0][2]]=1
  res+=1
  k+=temp*2
  taxy_x, taxy_y=passenger_end[cand[0][2]][0], passenger_end[cand[0][2]][1]
if not flag:
  print(-1)
else:
  print(k)
    