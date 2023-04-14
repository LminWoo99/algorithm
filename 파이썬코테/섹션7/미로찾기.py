from collections import deque
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
a=[list(map(int, input().split()))for _ in range(7)]
ch=[[0]*7 for _ in range(7)]
dq=deque()
dq.append((0,0))
a[0][0]=1
res, tmp=0, 0
while dq:
    tmp=dq.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and ch[x][y]==0:
            a[x][y]=1
            ch[x][y]=ch[tmp[0]][tmp[1]]+1
            dq.append((x,y))
if ch[6][6]==0:
    print(-1)
else:
    print(ch[6][6])
        
        
                
